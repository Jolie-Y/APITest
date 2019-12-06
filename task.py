# -*- coding: utf-8 -*-

import requests
import constant


def get_task_list(auth):
    json = {
      "act": "check",
      "detail": {
        "auth": auth,
        "meta": False,
      }
    }
    response = requests.post(constant.TASK_URL, json=json, timeout=constant.TIMEOUT)
    return response


def complete_task(auth, taskid):
    json = {
      "act": "trigger",
      "detail": {
        "auth": auth,
        "taskid": taskid,
      }
    }
    response = requests.post(constant.TASK_URL, json=json, timeout=constant.TIMEOUT)
    return response
