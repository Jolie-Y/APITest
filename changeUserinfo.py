# -*- coding: utf-8 -*-

import constant
import requests
from httpRequest import HttpRequest

#实名认证
def bindCard(auth,identitycard="450311197509088166",realname="测试"):
    json = {
        "act":"changeinfo",
        "detail":{
            "auth":auth,
            "identitycard":identitycard,
            "realname":realname
        }
    }
    #response = requests.post(constant.changeUserinfo,headers=constant.HEADERS,json=json)
    response = HttpRequest().http_request(constant.changeUserinfo,json,constant.HEADERS,"post")
    return response
    




#修改用户基本信息

def changeUserinfo(auth,avatar="https://ss1.baidu.com/-4o3dSag_xI4khGko9WTAnF6hhy/image/h%3D300/sign=a9e671b9a551f3dedcb2bf64a4eff0ec/4610b912c8fcc3cef70d70409845d688d53f20f7.jpg",name="ceshi",gender=0):
    json = {
        "act":"changeinfo",
        "detail":{
            "auth":auth,
            "avatar":avatar,
            "name":name,
            "gender":gender
        }
    }
    #response = requests.post(constant.changeUserinfo,headers=constant.HEADERS,json=json)
    response = HttpRequest().http_request(constant.changeUserinfo,json,constant.HEADERS,"post")
    getInfoResult = response.json()
    print(getInfoResult)
    realResult= getInfoResult["Result"]["success"]

    if getInfoResult["Result"]["success"]== True:
        username = getInfoResult["Result"]["detail"]["name"]
        usergender = getInfoResult["Result"]["detail"]["gender"]
        useravatar = getInfoResult["Result"]["detail"]["avatar"]
        return username,usergender,realResult,useravatar
    else:
        return realResult

