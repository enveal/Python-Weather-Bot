from config.config_reader import ConfigReader

class RoomRecommend():
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()

    def get_room_info(self,roomtype):
        self.roomtype = roomtype

        if roomtype in ['room', 'rooms']:
            self.bot_says = "Please describe more. What rooms are you looking?"
        else:
            # self.bot_says = "i didn't understand what you're saying.."
            self.bot_says = "ok, this room is suggested for you."
        return self.bot_says