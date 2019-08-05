import datetime
import calendar
import schedule
import time

from utils import Utils


class C3pO:
    def __init__(self, logger):
        self.logger = logger
        self.func = Utils(logger)
        self.update = ""
        self.bot = ""


    def validate_c3po(self):
        bot = self.bot
        update = self.update

        self.func.insert_request(update)

        try:
            now = datetime.datetime.now()
            self.func.logar("Agora... são.. exatamente... %s..." % now.strftime('%H:%M:%S'))

            sent_msg = False
            qnt_dias_mes = calendar.monthrange(now.year, now.month)[1]

            data = datetime.datetime.now()
            dia_hoje = int(data.strftime('%d'))

            if dia_hoje == 20 or dia_hoje == qnt_dias_mes or self.func.dias_uteis() == 5:
                sent_msg = True

            if sent_msg:
                update.message.reply_text('Atenção: Hoje é dia %s. Dia de maior volume de envios de '
                                          'SMS/E-MAIL. Monitorar!'
                                          % dia_hoje)

                self.func.logar("Atenção: Hoje é dia %s. Dia de maior volume de envios de SMS/E-MAIL. Monitorar!")

            else:
                update.message.reply_text(
                    "Ainda... não... é... a... hora... certa... aguardando... até... amanhã...")
                self.func.logar("Ainda... não... é... a... hora... certa... aguardando... até... amanhã...")

            return True

        except Exception as err:
            update.message.reply_text("Erro no C3PO: %s" % err)
            self.func.logar("[RIP] C3PO foi morto em combate: %s" % err, "CRITICAL")
            self.func.logar("------------------------------------------")

    def control_bot(self, bot, update):
        self.bot = bot
        self.update = update

        try:
            schedule.every().day.at("08:00").do(self.validate_c3po)

            self.func.logar("Schedules OK")
            while True:
                schedule.run_pending()
                time.sleep(1)
        except Exception as err:
            print(err)
