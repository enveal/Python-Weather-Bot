from config.config_reader import ConfigReader

class RoomRecommend():
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()

    def get_room_info(self,roomtype):
        self.roomtype = roomtype

        self.bot_says = "This "+str(roomtype) + " room is suggested for you."
        return self.bot_says