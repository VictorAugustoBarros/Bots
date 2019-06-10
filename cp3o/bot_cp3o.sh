#!/bin/sh

SERVICE='/integracao/sorocred/email/sorocred_cejud_email.py'
if ps ax | grep -v grep | grep -v daemon | grep -v log | grep $SERVICE > /dev/null
then
   echo "..."
else
   $SERVICE &
fi
