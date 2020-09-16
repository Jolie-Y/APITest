# -*- coding: utf-8 -*-

import requests
import constant
from httpRequest import HttpRequest
from hmacsha256 import hmac_sha256
import time
import random

def get_task_list(auth):
    json = {
      "act": "check",
      "detail": {
        "auth": auth,
        "meta": False,
      }
    }
    #response = requests.post(constant.TASK_URL, json=json, timeout=constant.TIMEOUT)
    response = HttpRequest().http_request(constant.TASK_URL,json,constant.HEADERS,"post")
    return response


def complete_task(auth, taskid):
    json = {
      "act": "trigger",
      "detail": {
        "auth": auth,
        "taskid": taskid,
      }
    }
    #response = requests.post(constant.TASK_URL, json=json, timeout=constant.TIMEOUT)
    response = HttpRequest().http_request(constant.TASK_URL,json,constant.HEADERS,"post")
    return response


def VideosmallGame(auth,appid="youliao",reason="game2344adroi"):
    stick = time.time()
    ts = int(round(stick*1000))
    coin = random.randint(450,500)
    canshuo = str(coin)+reason+auth+str(ts)
    secret = hmac_sha256(canshuo)
    print(secret)
    print(coin)
    json = {
      "appid":appid,
      "token":auth,
      "secret":secret,
      "ts":ts,
      "coin":coin,
      "reason":reason
    }
    response = HttpRequest().http_request(constant.samllGame,json,constant.HEADERS,"post")
    return response
      

def smallGame(auth,appid="youliao",reason="game2344feed"):
    stick = time.time()
    ts = int(round(stick*1000))
    coin = random.randint(1,10)
    canshuo = str(coin)+reason+auth+str(ts)
    secret = hmac_sha256(canshuo)
    print(secret)
    print(coin)
    json = {
      "appid":appid,
      "token":auth,
      "secret":secret,
      "ts":ts,
      "coin":coin,
      "reason":reason
    }
    response = HttpRequest().http_request(constant.samllGame,json,constant.HEADERS,"post")
    return response
      
