#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Bot Responsável por alertar os dias com maior número de disparos nos seguintes dias:
# - 5 dia útil do mês
# - Dia 20
# - Ultimo da do mês

# API bot: 775230963:AAHDhyGD-05hps3p0tDajqJGV9GCDBDmhpE
# Chat ID: -343218807
# Grupo: DEV - INTEG & Tradutor


import time
import logging
import datetime
import calendar

from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(token='775230963:AAHDhyGD-05hps3p0tDajqJGV9GCDBDmhpE')
dispatcher = updater.dispatcher

# ----------------------------------------------- Logs ----------------------------------------------#
logger = logging.getLogger('c3po')
hdlr = logging.FileHandler('/var/log/bots/c3po.log')
pattern = "%(asctime)s | %(levelname)s | %(message)s"
formatter = logging.Formatter(pattern)
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


def dias_uteis():
    now = datetime.datetime.now()
    hoje = now.strftime('%d')
    utils_days = 0

    for i in range(0, int(hoje)):
        data = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=-i))

        if data.weekday() not in [0, 6]:
            utils_days = utils_days + 1

    return utils_days


def logar(msg, level='INFO'):
    if level == "INFO":
        logger.info(msg)
        print(msg)

    elif level == "CRITICAL":
        logger.critical(msg)
        print(msg)


def start(bot, update):
    try:
        while True:
            now = datetime.datetime.now()
            logar("Agora... são.. exatamente... %s..." % now.strftime('%H:%M:%S'))
            if int(now.strftime('%H')) == 8:
                sent_msg = False
                qnt_dias_mes = calendar.monthrange(now.year, now.month)[1]

                for i in range(0, qnt_dias_mes):
                    data = datetime.datetime.now()
                    dia_hoje = int(data.strftime('%d'))

                    if dia_hoje == 20 or dia_hoje == qnt_dias_mes or dias_uteis() == 5:
                        sent_msg = True

                    if sent_msg:
                        bot.sendMessage(chat_id=-343218807,
                                        text='Atenção: Hoje é dia %s. Dia de maior volume de envios de '
                                             'SMS/E-MAIL. Monitorar!'
                                             % dia_hoje)
                        logar("Atenção: Hoje é dia %s. Dia de maior volume de envios de SMS/E-MAIL. Monitorar!")

                    tomorrow = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=1),
                                                         hour=8, minute=0, second=0)

                    logar("Próxima... execução... amanhã.. às... %s... horas" % tomorrow)
                    delta = tomorrow - datetime.datetime.now()

                    time.sleep(delta.seconds)
                    continue

            uma_hora = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(hours=1))
            logar("Ainda... não... é... a... hora... certa... verificando... denovo... às... %s " % uma_hora.strftime(
                '%H:%M:%S'))

            delta = uma_hora - datetime.datetime.now()
            time.sleep(delta.seconds)

    except Exception as err:
        bot.sendMessage(chat_id=-343218807, text="Erro no C3PO: %s" % err)
        logar("[RIP] C3PO foi morto em combate: %s" % err, "CRITICAL")
        logar("------------------------------------------")


logar("------------------------------------------")
logar("Ligando o c3pO")

start_handler = CommandHandler('volume_mensal', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
