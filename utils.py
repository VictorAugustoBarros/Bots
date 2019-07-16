import datetime
import os


class Utils:
    def __init__(self, logger):
        self.logger = logger

    def dias_uteis(self):
        now = datetime.datetime.now()
        hoje = now.strftime('%d')
        utils_days = 0

        for i in range(0, int(hoje)):
            data = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=-i))

            if data.weekday() not in [0, 6]:
                utils_days = utils_days + 1

        return utils_days

    def logar(self, msg, level='INFO'):
        if level == "INFO":
            self.logger.info(msg)
            print(msg)

        elif level == "CRITICAL":
            self.logger.critical(msg)
            print(msg)

    def insert_request(self, data):
        os.chdir('../config/')
        with open("request.txt", "a+") as file:
            data_new = {
                "Datetime": str(data.message.date),
                "Chat_ID": data.message.chat_id,
                "Bot_Name": data.message.from_user.bot.name,
                "User": data.message.from_user.full_name
            }
            file.write(str(data_new) + "\n")
