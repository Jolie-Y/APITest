# -*- coding: utf-8 -*-

import requests
import constant
import time
import random
from httpRequest import HttpRequest

 #绑定邀请码任务

def bindmaster(auth,invcode="230331135"):
    json={
        "act":"bindmaster",
        "detail":{
            "auth":auth,
            "invcode":invcode
        }
    }

    #response = requests.post(constant.bindmasterUrl,headers=constant.HEADERS,json=json,timeout=constant.TIMEOUT)
    response = HttpRequest().http_request(constant.bindmasterUrl,json,constant.HEADERS,"post")
    return response



#阅读新闻任务

def readNews(auth,cnt="news",program="reading",url="https://droinews/1000"+str(random.randint(1,100))+".com"):
    time.sleep(30)
    json = {
        "auth":auth,
        "url":url,
        "actions":"NOP",
        "stay":30,
        "cnt":cnt,
        "program":program
    }
    #response = requests.post(constant.readingUrl,headers=constant.HEADERS,json=json)
    response = HttpRequest().http_request(constant.readingUrl,json,constant.HEADERS,"post")

    return response

#签到任务

def signIn(auth):
    json = {
        "act":"signin_v2",
        "detail":auth
    }
    #response = requests.post(constant.taskUrl,headers=constant.HEADERS,json=json)
    response = HttpRequest().http_request(constant.taskUrl,json,constant.HEADERS,"post")
    return response


#首次查看钱包,使用新任务系统
'''
def walletLooked(auth):
    json = {
        "act":"walletlooked",
        "detail":auth
    }
    response = requests.post(constant.taskUrl,headers=constant.HEADERS,json=json)
    return response
'''
#分享新闻任务

def shareCnt(auth,url="https://droinews/1000.com"):
    json = {
        "act":"sharecnt",
        "detail":{
            "auth":auth,
            "url":url
        }
    }
    time.sleep(30)
    #response = requests.post(constant.taskUrl,headers=constant.HEADERS,json=json)
    response = HttpRequest().http_request(constant.taskUrl,json,constant.HEADERS,"post")
    return response

 