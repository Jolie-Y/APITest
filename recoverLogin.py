import requests
import time
url = "http://106.15.234.82/tester/lock?tester="

 
#清除账号信息

def recoverUserLogin(phone):
    print(url + phone + "&lock=0")
    response = requests.get(url + phone + "&lock=0")
    return response

#re = recoverUserLogin("13615506715")

#print(re.json())