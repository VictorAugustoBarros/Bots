FROM python:3

MAINTAINER Victor e Léo

RUN mkdir -p /opt/bot_telegram

COPY . /opt/bot_telegram

WORKDIR /opt/bot_telegram

RUN pip install python-telegram-bot --upgrade

RUN pip install schedule

RUN chmod +x /opt/bot_telegram/main.py

RUN ln -snf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && echo America/Sao_Paulo > /etc/timezone

RUN /usr/local/bin/python3 /opt/bot_telegram/main.py --start