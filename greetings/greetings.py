from config.config_reader import ConfigReader
import random

class Greetings():
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()

    def get_greetings_response(self,greet):
        self.greet=greet
        bot_response = ['Hello, what can i do for you?', 'Hi..', 'Welcome User !!', 'What are you looking for there??']
        self.bot_says = random.choice(bot_response)
        return self.bot_says