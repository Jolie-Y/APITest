# -*- coding: utf-8 -*-

import requests
import constant

def login():
    json = {
        "act": "loginsms",
        "detail": {
            "phone": "13333333333",
            "verify": "111111",
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

    r = requests.post(constant.URL + "loginopt", json=json, headers=constant.HEADERS, verify=False)

    auth = ''

    if r.status_code == 200:
        json = r.json()
        auth = json['Result']['detail']['auth']

    return auth
