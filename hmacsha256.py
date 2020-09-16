import hmac
import hashlib
#import time


def hmac_sha256(ts,key="2631d42e8fadf2623207f4135e8acbec"):
    sign = hmac.new(bytes(str(key), encoding='utf-8'), bytes("youliao"+str(ts), encoding='utf-8'),digestmod=hashlib.sha256).digest()
    result = sign.hex()
    return result

'''
stick = time.time()
ts = int(round(stick*1000))

h = hmac_sha256(ts)
print(h)
'''