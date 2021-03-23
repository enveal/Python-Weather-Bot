from greetings.greetings import Greetings
from botbuilder.core import TurnContext,ActivityHandler
from botbuilder.ai.luis import LuisApplication,LuisPredictionOptions,LuisRecognizer
import json
from weather.weatherApp import WeatherInformation
from config.config_reader import ConfigReader
from roomRecommend.room_recommend import RoomRecommend
from greetings.greetings import Greetings

from logger.logger import Log
class LuisConnect(ActivityHandler):
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()
        self.luis_app_id=self.configuration['LUIS_APP_ID']
        self.luis_endpoint_key = self.configuration['LUIS_ENDPOINT_KEY']
        self.luis_endpoint = self.configuration['LUIS_ENDPOINT']
        self.luis_app = LuisApplication(self.luis_app_id,self.luis_endpoint_key,self.luis_endpoint)
        self.luis_options = LuisPredictionOptions(include_all_intents=True,include_instance_data=True)
        self.luis_recognizer = LuisRecognizer(application=self.luis_app,prediction_options=self.luis_options,include_api_results=True)
        self.log=Log()
 

    async def on_message_activity(self,turn_context:TurnContext):
        weather_info=WeatherInformation()
        greet_info = Greetings()
        room_recommend = RoomRecommend()
        luis_result = await self.luis_recognizer.recognize(turn_context)
        result = luis_result.properties["luisResult"]
        if result.entities:
            json_str = json.loads((str(result.entities[0])).replace("'", "\""))
        else:
            json_str = None
        if result.top_scoring_intent.intent == 'Greetings':
            if json_str is not None:
                greet_response = greet_info.get_greetings_response(json_str.get('entity'))
            else:
                greet_response = greet_info.get_greetings_response(json_str)

            self.log.write_log(sessionID='session1',log_message="Bot Says: "+str(greet_response))
            await turn_context.send_activity(f"{greet_response}")

        elif result.top_scoring_intent.intent == 'Weather':
            if json_str is not None:
                weather=weather_info.get_weather_info(json_str.get('entity'))
            else:
                weather=greet_info.get_none_response(json_str)

            self.log.write_log(sessionID='session1',log_message="Bot Says: "+str(weather))
            await turn_context.send_activity(f"{weather}")

        elif result.top_scoring_intent.intent == 'Options':
            if json_str is not None:
                option = greet_info.get_options_response(json_str.get('entity'))
            else:
                option =greet_info.get_none_response(json_str)

            self.log.write_log(sessionID='session1',log_message="Bot Says: "+str(option))
            await turn_context.send_activity(f"{option}")

        elif result.top_scoring_intent.intent == 'Thanks':
            if json_str is not None:
                thanks = greet_info.get_thanks_response(json_str.get('entity'))
            else:
                thanks = greet_info.get_none_response(json_str)

            self.log.write_log(sessionID='session1',log_message="Bot Says: "+str(thanks))
            await turn_context.send_activity(f"{thanks}")

        elif result.top_scoring_intent.intent == 'Goodbye':
            if json_str is not None:
                goodbye = greet_info.get_goodbye_response(json_str.get('entity'))
            else:
                goodbye = greet_info.get_none_response(json_str)
                    
            self.log.write_log(sessionID='session1',log_message="Bot Says: "+str(goodbye))
            await turn_context.send_activity(f"{goodbye}")

        elif result.top_scoring_intent.intent == 'roomRecommend':
            if json_str is not None:
                room_re = room_recommend.get_room_info(json_str.get('entity'))
            else:
                room_re = greet_info.get_none_response(json_str)
                
            self.log.write_log(sessionID='session1',log_message="Bot Says: "+str(room_re))
            await turn_context.send_activity(f"{room_re}")

        elif result.top_scoring_intent.intent == 'None':
            none_response = greet_info.get_none_response("none")
            self.log.write_log(sessionID='session1',log_message="Bot Says: "+str( none_response))
            await turn_context.send_activity(f"{none_response}")