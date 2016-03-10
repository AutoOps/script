#/bin/env python
#coding:utf-8
import re,os,time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT_FILE = BASE_DIR + "/conf/text.conf"

with open(TEXT_FILE,'r') as f:
        for i in f.readlines():
                if not re.findall("TEXT_INFO",i):
                        exec (i.strip())

NOW_TIME = time.strftime("%Y%m%d%H%M")
#YmdHM_TIME = time.strftime("%Y%m%d%H%M")
Ymd_TIME = time.strftime("%Y%m%d")
YmdHMS_TIME = time.strftime("%Y-%m-%d %H:%M:%S")
LOG_DIR = BASE_DIR + "/logs/"
LOG_INFO = LOG_DIR + INFO_TEXT

#print LOG_DIR
#print LOG_INFO
def writeLog(applogs):
	local_logs = applogs
	if not os.path.exists(LOG_DIR):
		os.mkdir(LOG_DIR)
	file = open(LOG_DIR + Ymd_TIME + SUFFIX_TEXT,"a")
	file.write(local_logs)
	file.close()

def dealLog():
	with open(LOG_INFO,'r') as f:
		msg = f.read()
		msg = msg.replace('Enter',ENTER_TEXT)
#		log = TIME_TEXT + ENTER_TEXT + YmdHMS_TIME + ENTER_TEXT + SUBJECT_TEXT + ENTER_TEXT + msg + ENTER_TEXT
#		writeLog(log)
		writeLog(msg)
		os.remove(LOG_INFO)
		return msg

def logApp():
	return dealLog()
