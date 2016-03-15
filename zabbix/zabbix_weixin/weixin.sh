#!/bin/bash
BASE_DIR=$(cd $(dirname ${0});pwd)
FILE="${BASE_DIR}/monitor_weixin/logs/tmpinfo.txt"
SCRIPT="${BASE_DIR}/monitor_weixin/manage.py"
echo $FILE
echo $SCRIPT
while [ -d $BASE_DIR ]
do
	if [ -f $FILE ];then
	        env python $SCRIPT
	        continue
	else
	        echo $1 > $FILE
	        env python $SCRIPT
	fi
	exit
done
