# -*- coding: utf-8 -*-

import requests
import constant
from httpRequest import HttpRequest


def login(phone: str, verify: str):
    json = {
        "act": "loginsms",
        "detail": {
            "phone": phone,
            "verify": verify,
            "channel": "Test",
            "fincode": "TOP_QUJIE",
            "device": {
                "uuid": "b5a96fffa5c30d2b32fdd5dc71da3498",
                "ip": "192.168.3.45",
                "mac": "56:E8:56:CD:4F:35",
                "city": "上海",
                "mutexid": "617e8517b7f242fdc9d53c0e0969467c",
                "freeme": {},
                "soc": " Qualcomm Technologies, Inc SDM845",
                "osver": "10",
                "model": "ONEPLUS A6000",
                "brand": "OnePlus"
            }
        }
    }

    #response = requests.post(constant.BAAS_URL + "loginopt", json=json, headers=constant.HEADERS, timeout=constant.TIMEOUT)
    response = HttpRequest().http_request(constant.BAAS_URL + "loginopt",json,constant.HEADERS,"post")

    auth = None

    if response.status_code == 200:
        json = response.json()
        print(json)
        result = json['Result']
        if result is not None and json['Code'] == 0 and result['success'] and result['detail'] is not None:
            auth = result['detail']['auth']
            invcode = result["detail"]["invcode"]
            return auth,invcode
        else:
            return json

def get_user_info(auth):
    json = {
        "act": "refresh",
        "detail": auth
    }
    #response = requests.post(constant.BAAS_URL + "loginopt", json=json, headers=constant.HEADERS, timeout=constant.TIMEOUT)
    response = HttpRequest().http_request(constant.BAAS_URL + "loginopt",json,constant.HEADERS,"post")
    return response


def get_phoneIdentifingCode(phone):
    json = {
        "act":"verify",
        "detail":{
            "phone":phone
        }
    }
    #response = requests.post(constant.loginUrl,headers=constant.HEADERS,json=json)
    response = HttpRequest().http_request(constant.loginUrl,json,constant.HEADERS,"post")
    return response

def get_masterNickName(auth):
    json = {
        "act":"master",
        "detail":auth
    }
    #response = requests.post(constant.loginUrl,headers=constant.HEADERS,json=json)
    response = HttpRequest().http_request(constant.loginUrl,json,constant.HEADERS,"post")
    result = response.json()
    success = result["Result"]["success"]
    if success:
        return result["Result"]["detail"]
    else:
        return success


#查询徒弟贡献榜
def get_slaverFeed(auth):
    json = {
        "act":"slaverfeed",
        "detail":{
            "auth":auth
            }
    }
    #response = requests.post(constant.bindmasterUrl,headers=constant.HEADERS,json=json)
    response = HttpRequest().http_request(constant.bindmasterUrl,json,constant.HEADERS,"post")
    return response


#查询用户全部好友
def get_allFriends(auth):
    json = {
        "act":"allFriends",
        "detail":{
            "auth":auth
        }
    }
    #response = requests.post(constant.bindmasterUrl,headers=constant.HEADERS,json=json)
    response = HttpRequest().http_request(constant.bindmasterUrl,json,constant.HEADERS,"post")
    return response

#查询金币明细
def get_goldLogDay(auth):
    json = {
        "act":"goldlogday",
        "detail":{
            "auth":auth
        }
    }
    #response = requests.post(constant.bindmasterUrl,headers=constant.HEADERS,json=json)
    response = HttpRequest().http_request(constant.bindmasterUrl,json,constant.HEADERS,"post")
    return response
'''
#查询用户今日金币实时变化
def get_goldToday(auth):
    json = {
        "act":"goldtoday",
        "detail":auth
    }
    response = requests.post(constant.bindmasterUrl,headers=constant.HEADERS,json=json)
    return response
'''

def get_goldToday(auth):
    json = {
        "act":"goldtoday",
        "detail":auth
    }
    #response = requests.post(constant.bindmasterUrl,headers=constant.HEADERS,json=json)
    #return response
    re = HttpRequest().http_request(constant.bindmasterUrl,json,constant.HEADERS,"post")
    return re