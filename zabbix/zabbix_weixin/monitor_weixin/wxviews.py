#/bin/env python
#coding:utf-8
import os,re,json
import httplib,urllib,urllib2

#读取配置
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = CONFIG_DIR + "/conf/interface.conf"
TEXT_FILE = CONFIG_DIR + "/conf/text.conf"

with open(CONFIG_FILE,'r') as f:
	for i in f.readlines():
		if not (re.findall("ACCESSTOKEN",i) or re.findall("APPMSG",i)):
			exec (i.strip())

with open(TEXT_FILE,'r') as f:
	for i in f.readlines():
		if not re.findall("TEXT_INFO",i):
			exec (i.strip())

#获取令牌
def getToken():
	params = urllib.urlencode({'corpid':CorpID,'corpsecret':Secret})
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	httpClient = httplib.HTTPSConnection('qyapi.weixin.qq.com',443)
	httpClient.request("POST", "/cgi-bin/gettoken?", params, headers)
	response = httpClient.getresponse()
	ret = response.read()
	token = json.loads(ret)['access_token']
	httpClient.close()
	return token.encode('utf-8')

#发送信息
def sendMsg(token,content,user,id):
#	print token
	data = {
		"touser":user,
		"msgtype":"text",
		"agentid":id,
		"text":{
			"content":content,
			},
		"safe":"0",
	}
	data = json.dumps(data,ensure_ascii=False)
	req = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s'%(token,),data)
	resp = urllib2.urlopen(req)
	msg = resp.read()
	return STATUS_TEXT + msg + ENTER_TEXT

def weiXin(message):
	return sendMsg(getToken(),message,user,id)
