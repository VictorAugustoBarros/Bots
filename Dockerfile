FROM python:alpine3.6

MAINTAINER Victor e Léo

RUN mkdir -p /opt/bot_telegram

RUN mkdir -p /opt/bot_telegram/cron/

COPY . /opt/bot_telegram

WORKDIR /opt/bot_telegram

RUN apk --update add python py-pip openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && apk del build-dependencies

RUN apk add --no-cache --virtual .py_deps build-base python3-dev libffi-dev openssl-dev

RUN pip3 install python-telegram-bot

RUN apk update && apk add tzdata &&\
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime &&\
    echo "America/Sao_Paulo" > /etc/timezone &&\
    apk del tzdata && rm -rf /var/cache/apk/*

CMD chown root:root /etc/crontabs/root && /usr/sbin/crond -f

RUN chmod 777 /opt/bot_telegram/main.py

CMD /opt/bot_telegram/main.py --start