import random
import user
import taskRequest
from deleteAccount import deleteAc

'''
#生成多个手机号码
phoneNumber=[]


for i  in range(1,2):
    phone = str(random.choice(['139', '188', '185', '136', '158', '151', '176', '137']) +"".join(random.choice("0123456789") for i in range(8)))
    phoneNumber.append(phone)

print(phoneNumber)

'''

#生成一个手机号码
'''
phone = str(random.choice(['139', '188', '185', '136', '158', '151', '176', '137']) +"".join(random.choice("0123456789") for i in range(8)))


#新增1个徒弟
 

auth = user.login(phone,"222222")

userauth = auth[0]
'''

def add_slaver(invcode):
    phone = str(random.choice(['139', '188', '185', '136', '158', '151', '176', '137']) +"".join(random.choice("0123456789") for i in range(8)))
    deleteAc(phone)
    auth = user.login(phone,"222222")
    userauth = auth[0]
    result = taskRequest.bindmaster(userauth,invcode)
    return result

#add_slaver("276538260")
