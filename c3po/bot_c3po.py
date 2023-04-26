import datetime
import calendar
import schedule
import time
import json

from utils import Utils


class C3pO:
    def __init__(self, logger):
        self.logger = logger
        self.func = Utils(logger)
        self.update = ""
        self.bot = ""

    def validate_c3po(self):
        chat_id = []
        for reg in open('config/request.txt', 'r').readlines():
            json_tmp = json.loads(reg)
            chat_id.append(json_tmp['Chat_ID'])

        chat_id = set(chat_id)
        bot = self.bot
        update = self.update

        try:
            now = datetime.datetime.now()

            sent_msg = False
            qnt_dias_mes = calendar.monthrange(now.year, now.month)[1]

            data = datetime.datetime.now()
            dia_hoje = int(data.strftime('%d'))

            if dia_hoje == 20 or dia_hoje == qnt_dias_mes or self.func.dias_uteis() == 5:
                sent_msg = True

            if sent_msg:
                for id in chat_id:
                    self.bot.send_message(id,
                                          'Atenção: Hoje é dia %s. Dia de maior volume de envios de '
                                          'SMS/E-MAIL. Monitorar!'
                                          % dia_hoje)

                self.func.logar("Atenção: Hoje é dia %s. Dia de maior volume de envios de SMS/E-MAIL. Monitorar!")

            else:
                for id in chat_id:
                    self.bot.send_message(id, 'Hoje é apenas um dia normal !')

                self.func.logar("Hoje é apenas um dia normal !")

            return True

        except Exception as err:
            update.message.reply_text("Erro no C3PO: %s" % err)
            self.func.logar("[RIP] C3PO foi morto em combate: %s" % err, "CRITICAL")
            self.func.logar("------------------------------------------")

    def control_bot(self, bot, update):
        self.func.insert_request(update)
        self.bot = bot
        self.update = update

        try:
            schedule.every().day.at("10:30").do(self.validate_c3po)
            schedule.every(5).seconds.do(self.validate_c3po)

            while True:
                schedule.run_pending()
                print(datetime.datetime.now())
                time.sleep(1)
        except Exception as err:
            print(err)
