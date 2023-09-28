

from telegram.ext import Updater
from telegram.ext import CommandHandler

from datetime import datetime
import argparse
import logging
import schedule
import threading
import time
from utils import Utils
from c3po.bot_c3po import C3pO

if __name__ == "__main__":

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
    bot_token = "885441367:AAGwhasqgMux9acW5kHhB5YzgX1hdNjaThA"

    updater = Updater(token=bot_token)

    func = Utils(logger)
    c3po = C3pO(logger)

    args = argparse.ArgumentParser(description='Main')

    group = args.add_mutually_exclusive_group(required=True)

    group.add_argument('--start', action='store_true', help='Register Chat ID')
    group.add_argument('--c3po', action='store_true', help='Start bot c3po')

    if args.parse_args().start is True:
        print("Registrando usuário ...")
        updater.dispatcher.add_handler(CommandHandler('start', c3po.control_bot))
        updater.start_polling(clean=True)
        updater.idle()
