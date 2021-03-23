from config.config_reader import ConfigReader
import random


class Greetings():
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()

    def get_greetings_response(self, greet):
        self.greet = greet
        bot_response = ['Hi there! My name is echo-bot, I’ll be happy to assist you right away!', 'Hello, thanks for asking',
                        'Good to see you again', 'Hi there, how can I help?']
        self.bot_says = random.choice(bot_response)
        return self.bot_says

    def get_thanks_response(self, thanks):
        self.thanks = thanks
        bot_response = [
            "Happy to help!",
            "Any time!",
            "My pleasure"
        ]
        self.bot_says = random.choice(bot_response)
        return self.bot_says

    def get_goodbye_response(self, goodbye):
        self.greet = goodbye
        bot_response = ["See you!", "Have a nice day",
                        "Bye! Come back again soon."]

        self.bot_says = random.choice(bot_response)
        return self.bot_says

    def get_none_response(self, message):
        self.message = message
        bot_response = [
            "Sorry, can't understand you",
            "Please give me more info",
            "Not sure I understand"
        ]

        self.bot_says = random.choice(bot_response)
        return self.bot_says

    def get_options_response(self, option):
        self.option = option
        bot_response = [
            "I can guide you through Adverse drug reaction list, Blood pressure tracking, Hospitals and Pharmacies",
            "Offering support for Adverse drug reaction, Blood pressure, Hospitals and Pharmacies"
        ]
        self.bot_says = random.choice(bot_response)
        return self.bot_says
