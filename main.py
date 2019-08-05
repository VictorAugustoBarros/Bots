#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Bot Responsável por alertar os dias com maior número de disparos nos seguintes dias:
# - 5 dia útil do mês
# - Dia 20
# - Ultimo da do mês

# API bot: 775230963:AAHDhyGD-05hps3p0tDajqJGV9GCDBDmhpE
# Chat ID: -343218807
# Grupo: DEV - INTEG & Tradutor

from telegram.ext import Updater
from telegram.ext import CommandHandler

from datetime import datetime
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

    # C3PO
    # bot_token = "775230963:AAHDhyGD-05hps3p0tDajqJGV9GCDBDmhpE"

    # Teste
    bot_token = "885441367:AAFcrnwIajbP-RYKN2Wzn87OHiJuD56Qq8I"

    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher

    func = Utils(logger)
    c3po = C3pO(logger)

    args = argparse.ArgumentParser(description='Main')

    group = args.add_mutually_exclusive_group(required=True)

    group.add_argument('--c3po', action='store_true', help='Start bot c3po')

    if args.parse_args().c3po is True:
        start_handler = CommandHandler('volume_mensal', c3po.control_bot)
        dispatcher.add_handler(start_handler)
        updater.start_polling()
