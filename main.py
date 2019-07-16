#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Bot Responsável por alertar os dias com maior número de disparos nos seguintes dias:
# - 5 dia útil do mês
# - Dia 20
# - Ultimo da do mês

# API bot: 775230963:AAHDhyGD-05hps3p0tDajqJGV9GCDBDmhpE
# Chat ID: -343218807
# Grupo: DEV - INTEG & Tradutor

print("Teste OK")

from telegram.ext import Updater
from telegram.ext import CommandHandler

import argparse
import logging
from utils import Utils
from c3po.bot_c3po import C3pO

if __name__ == "__main__":
    print("Ligando o c3pO")

    # ----------------------------------------------- Logs ----------------------------------------------#
    logger = logging.getLogger('c3po')
    hdlr = logging.FileHandler('c3po/c3po.log')
    pattern = "%(asctime)s | %(levelname)s | %(message)s"
    formatter = logging.Formatter(pattern)
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    # ---------------------------------------------------------------------------------------------------#

    bot_token = "775230963:AAHDhyGD-05hps3p0tDajqJGV9GCDBDmhpE"

    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher

    func = Utils(logger)
    c3po = C3pO(logger)

    args = argparse.ArgumentParser(description='Main')

    group = args.add_mutually_exclusive_group(required=True)
    group.add_argument('--start', action='store_true', help='Start bot')
    group.add_argument('--volume', action='store_true', help='Executa o script do bot')

    if args.parse_args().start is True:
        print("Start ...")
        start_handler = CommandHandler('start', c3po.start_c3po)
        dispatcher.add_handler(start_handler)
        updater.start_polling()

    if args.parse_args().volume is True:
        print("Volume Mensal ...")
        start_handler = CommandHandler('volume_mensal', c3po.validate_c3po)
        dispatcher.add_handler(start_handler)
        updater.start_polling()
