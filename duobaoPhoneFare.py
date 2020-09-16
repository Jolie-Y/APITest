import constant
from httpRequest import HttpRequest
from hmacsha256 import hmac_sha256
import time

def goodsExchange(auth,appid="youliao"):
    stick = time.time()
    ts = int(round(stick*1000))
    secret = hmac_sha256(ts)
    print(secret)
    json = {
        "token":auth,
        "appid":appid,
        "secret":secret,
        "ts":ts
    }

    response = HttpRequest().http_request(constant.duobaoPhoneFare,json,constant.HEADERS,"post")
    return response