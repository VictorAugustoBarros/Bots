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
import datetime
import calendar

from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(token='775230963:AAHDhyGD-05hps3p0tDajqJGV9GCDBDmhpE')
dispatcher = updater.dispatcher


def dias_uteis():
    now = datetime.datetime.now()
    hoje = now.strftime('%d')
    utils_days = 0

    for i in range(0, int(hoje)):
        data = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=-i))

        if data.weekday() not in [0, 6]:
            utils_days = utils_days + 1

    return utils_days


def start(bot, update):
    while True:
        now = datetime.datetime.now()

        if int(now.strftime('%H')) == 8:
            sent_msg = False
            hoje = now.strftime('%d')
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

                tomorrow = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=1),
                                                     hour=8, minute=0, second=0)
                print("Próxima Execução: %s " % tomorrow)
                delta = tomorrow - datetime.datetime.now()
                time.sleep(delta.seconds)
                continue

        uma_hora = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(hours=1))
        print("Próxima Execução: %s " % uma_hora)
        delta = uma_hora - datetime.datetime.now()
        time.sleep(delta.seconds)


start_handler = CommandHandler('volume_mensal', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
