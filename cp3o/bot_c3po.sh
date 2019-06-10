#!/bin/sh

SERVICE='/integracao/bot_telegram/cp3o/bot_c3po.py'
if ps ax | grep -v grep | grep -v daemon | grep -v log | grep $SERVICE > /dev/null
then
   echo "..."
else
   $SERVICE &
fi
