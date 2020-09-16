import requests,time
import random
import constant
from httpRequest import HttpRequest

def Prize(loginAuth,authMd5):
    json = {
        "token":loginAuth,
        "sign":authMd5,
        "times":random.randint(1,10)
    }
    time.sleep(30)
    #response = requests.get(constant.dzpUrl,params=json)
    response = HttpRequest().http_request(constant.dzpUrl,json,None,"get")
    #result = response.json()
    return response
