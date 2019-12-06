# -*- coding: utf-8 -*-

import requests
import constant


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

    response = requests.post(constant.BAAS_URL + "loginopt", json=json, headers=constant.HEADERS, timeout=constant.TIMEOUT)

    auth = None

    if response.status_code == 200:
        json = response.json()
        print(json)
        result = json['Result']
        if result is not None and json['Code'] == 0 and result['success'] and result['detail'] is not None:
            auth = result['detail']['auth']

    return auth


def get_user_info(auth):
    json = {
        "act": "refresh",
        "detail": auth
    }
    response = requests.post(constant.BAAS_URL + "loginopt", json=json, headers=constant.HEADERS, timeout=constant.TIMEOUT)
    return response
