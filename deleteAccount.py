import requests
import time
url = "http://106.15.234.82/tester/delete?"

 
#清除账号信息

def deleteAc(phone):
    response = requests.get(url + phone)
    result = response.json()
    if result["success"]:
        print("账号清除成功------------------")
        time.sleep(30)
    else:
        print("账号不存在------------------")

#deleteAc("13615506716")