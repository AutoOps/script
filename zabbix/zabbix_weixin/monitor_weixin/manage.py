#/bin/env python
#coding:utf-8
from wxviews import weiXin
from models.getNews import logApp,writeLog

writeLog(weiXin(logApp()))
