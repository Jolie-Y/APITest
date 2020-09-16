from user import login
import task
from taskRequest import bindmaster,readNews,signIn,shareCnt
#from user import get_user_info,get_phoneIdentifingCode,get_masterNickName,get_slaverFeed,get_allFriends,get_goldLogDay
import time
from deleteAccount import deleteAc
from changeUserinfo import changeUserinfo,bindCard
from md5 import md5Encode
from dzpPrize import Prize
import user
import userLogoff
import duobaoPhoneFare
#deleteAc("13818584511")
re = login("13818584524","111111")
print(re)


auth = re[0]
invode = re[1]

#print(re[1])


'''
info = get_user_info(re)
print(info.json())


ta = get_task_list(re)
print(ta.json())


com = complete_task(re,'first-wallet')
print(com.json())
print(com.status_code)


mas = bindmaster(re)
print(mas.status_code)
print(mas.json())



read = readNews(re)
print(read.status_code)
print(read.json())

time.sleep(30)
read = readNews(re)
print(read.status_code)
print(read.json())


sign = signIn(re)
print(sign.status_code)
print(sign.json())



wa = walletLooked(re)
print(wa.json())

sh = shareCnt(re)
print(sh.json())

qy = apkDownQY(re)
print(qy.json())

ad = adroiAdReward(re)
print(ad.json())



ta = get_task_list(re)
print(ta.json())


 

read = readNews(re)
print(read.status_code)
print(read.json())



com = complete_task(re,'adroi-video')
print(com.json())
print(com.status_code)



read = readNews(re)
print(read.status_code)
print(read.json())

sh = shareCnt(re)
print(sh.json())



com = complete_task(re,'adroi-video')
print(com.json())
print(com.status_code)


singlelogin = re + "ZYK_ac17c4b0bb1d5130bf8e0646ae2b4eb4"
singleauthMD5 = md5Encode(singlelogin.encode("UTF-8"))

dzp = Prize(re,singleauthMD5)

print(dzp)
 

phone = get_phoneIdentifingCode("13681695312")
print(phone.json())


name = get_masterNickName(re)
print(name.json())


phone = get_phoneIdentifingCode("13681695312")
print(phone.json())


name = get_masterNickName(re)
print(name.json())

re = get_slaverFeed(re)
print(re.json())

info = changeUserinfo(auth)
print(info)



allv = get_allFriends(auth)
print(allv.json())


mas = bindmaster(auth)
print(mas.status_code)
print(mas.json())


today1 = user.get_goldToday(auth)
print(today1.json())

read = readNews(auth)
print(read.status_code)
print(read.json())



today = user.get_goldToday(auth)
print(today.json())

jilu = user.get_goldLogDay(auth)
print(jilu.json())


response = task.complete_task(auth, 'dzp-video')
print(response.json())


response1 = task.complete_task(auth,"first-wallet")
print(response1.json())


response2 = task.complete_task(auth,"show-income")
print(response2.json())


response3 = task.complete_task(auth,"show-income#show_video")
print(response3.json())


response4 = task.complete_task(auth,"sign-video")
print(response4.json())

response5 = task.complete_task(auth,"bind-master#show_video")
print(response5.json())

response6 = task.complete_task(auth,"bind-phone#show_video")

print(response6.json())


re = bindCard(auth,realname="韩鹤松")
print(re.json())

ree = changeUserinfo(auth)
print(ree)

re = bindCard(auth,realname="哈哈哈哈哈哈哈")
print(re.json())

sign = signIn(auth)
print(sign.status_code)
print(sign.json())

read = readNews(auth)
print(read.status_code)
print(read.json())

gold = user.get_goldToday(auth)
print(gold.json())



response = task.complete_task(self.auth, 'dzp-video')
print(response.status_code())

singlelogin = auth + "ZYK_ac17c4b0bb1d5130bf8e0646ae2b4eb4"
singleauthMD5 = md5Encode(singlelogin.encode("UTF-8"))

dzp = Prize(re,singleauthMD5)

print(dzp)
'''
#useinfo = changeUserinfo(auth,name="111111111111111111111")

#res = user.get_slaverFeed(auth)
#print(res.json())

#response = task.complete_task(auth,"first-wallet")
#print(response.json())

#resv= userLogoff.userLogOff(auth)
#print(resv.json())

#game = task.smallGame(auth)
#print(game.json())


#videogame = task.VideosmallGame(auth)
#print(videogame.json())

#vs = duobaoPhoneFare.goodsExchange(auth)
#print(vs.json())

'''
read = readNews(auth)
print(read.status_code)
print(read.json())


ta = task.get_task_list(auth)
print(ta.json())
'''

#sh = shareCnt(auth)
#print(sh.json())




#response = task.complete_task(auth, 'first-share-news')
#print(response.json())
#--------------------新服务端测试-------------------------------
mas = bindmaster(auth)
print(mas.status_code)
print(mas.json())


#sign = signIn(auth)
#print(sign.status_code)
#print(sign.json())

#response = task.complete_task(auth,"sign-video")
#print(response.json())

#singlelogin = auth + "ZYK_ac17c4b0bb1d5130bf8e0646ae2b4eb4"
#singleauthMD5 = md5Encode(singlelogin.encode("UTF-8"))


#dzp = Prize(auth,singleauthMD5)

#print(dzp.json())