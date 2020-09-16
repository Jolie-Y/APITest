#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import user
import task
import time
import constant
from taskRequest import bindmaster,readNews,signIn,shareCnt
from deleteAccount import deleteAc
from changeUserinfo import bindCard,changeUserinfo
from md5 import md5Encode
from dzpPrize import Prize
import autoPhone
from httpRequest import HttpRequest
import random
import userLogoff
import recoverLogin



class TestUserMethods(unittest.TestCase):
    auth = ""

    def test_get_user_info(self):
        response = user.get_user_info(self.auth)
        self.assertEqual(200, response.status_code)
        json = response.json()
        self.assertEqual(self.auth, json['Result']['detail']['auth'])


class TestTaskMethods(unittest.TestCase):
    auth = ""

    def test_get_task_list(self):
        response = task.get_task_list(self.auth)
        self.assertEqual(200, response.status_code)
        json = response.json()
        print(json)
        self.assertTrue(json['success'])
    

    #大转盘看视频任务
    def test_complete_task(self):
        dzpCount = 3
        for i in range(3):
            response = task.complete_task(self.auth, 'dzp-video')
            self.assertEqual(200,response.status_code)
            json = response.json()
            print(json)
            self.assertTrue(json['success'])
            self.assertEqual(300,json["detail"]["gold"])
            count = json["detail"]["count"]
            dzpCount = dzpCount - 1
            self.assertEqual(dzpCount,count)

    #观看adroi广告任务
    def test_adroiVideo(self):
        Adroicount = 3
        for i in range(3):
            response = task.complete_task(self.auth,"adroi-video")
            self.assertEqual(200,response.status_code)
            result = response.json()
            print(result)
            self.assertTrue(result["success"])
            self.assertEqual(100,result["detail"]["gold"])
            surplusCount = result["detail"]["count"]
            print(surplusCount)
            Adroicount -= 1
            self.assertEqual(Adroicount,surplusCount)
            print("--------------------------------")

    
    #观看斗地主视频
    def test_ddzVideo(self):
        count = 3
        for i in range(3):
            response = task.complete_task(self.auth,"ddz-video")
            self.assertEqual(200,response.status_code)
            result = response.json()
            print(result)
            self.assertTrue(result["success"])
            self.assertEqual(300,result["detail"]["gold"])
            remainCount = result["detail"]["count"]
            count -= 1
            self.assertEqual(count,remainCount)
            


    #首次查看钱包任务
    def test_AfirstWallet(self):
        response = task.complete_task(self.auth,"first-wallet")
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        self.assertTrue(result["success"])
        self.assertEqual(808,result["detail"]["gold"])

    #有且只能做一次查看钱包任务
    def test_BfirstWallet(self):
        response = task.complete_task(self.auth,"first-wallet")
        result = response.json()
        self.assertFalse(result["success"])
        self.assertEqual("Error REST code [713000000] - task already closed",result["msg"])

    #晒收入
    def test_showIncome(self):
        print("晒收入----------------------------------------")
        response = task.complete_task(self.auth,"show-income")
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        self.assertTrue(result["success"])
        self.assertEqual(0,result["detail"]["count"])
        self.assertEqual(111,result["detail"]["gold"])

    #晒收入看视频
    def test_showincomeVideo(self):
        print("晒收入看视频-----------------------------------")
        response = task.complete_task(self.auth,"show-income#show_video")
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        count = result["detail"]["count"]
        self.assertEqual(0,count)
        self.assertEqual(203,result["detail"]["gold"])

    #签到视频
    def test_signVideo(self):
        print("签到看视频-------------------------------------")
        response = task.complete_task(self.auth,"sign-video")
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        self.assertTrue(result["success"])
        self.assertEqual(0,result["detail"]["count"])
        self.assertEqual(200,result["detail"]["gold"])

    #绑定邀请码看视频
    def test_bindmasterVideo(self):
        print("绑定邀请码看视频-----------------------")
        response = task.complete_task(self.auth,"bind-master#show_video")
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        self.assertTrue(result["success"])
        #self.assertEqual(0,result["detail"]["count"])
        self.assertEqual(301,result["detail"]["gold"])

    #绑定手机号码看视频
    def test_bindphoneVideo(self):
        print("绑定手机号码看视频-------------------------")
        response = task.complete_task(self.auth,"bind-phone#show_video")
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        self.assertTrue(result["success"])
        #self.assertEqual(0,result["detail"]["count"])
        self.assertEqual(302,result["detail"]["gold"])



class TestBindMaster(unittest.TestCase):
    auth = ""

    def test_bindmaster(self):
        #邀请码不存在
        response = bindmaster(self.auth,"000000000")
        self.assertEqual(200,response.status_code)
        print(response.json())
        self.assertEqual(False,response.json()["Result"]["success"])

        #绑定比自己晚注册的用户
        phone = str(random.choice(['139', '188', '185', '136', '158', '151', '176', '137']) +"".join(random.choice("0123456789") for i in range(8)))
        code  = user.login(phone,"222222")
        response = bindmaster(self.auth,code[1])
        result = response.json()
        self.assertFalse(result["Result"]["success"])
        self.assertEqual("Error in module [L50] code [615001002] - invalid younger master",result["Result"]["msg"])


        #邀请码正常
        response = bindmaster(self.auth)
        self.assertEqual(200,response.status_code)
        print(response.json())
        self.assertEqual(True,response.json()["Result"]["success"])

        #用户已绑定过邀请码
        response = bindmaster(self.auth)
        self.assertEqual(200,response.status_code)
        print(response.json())
        self.assertEqual(-615006003,response.json()["Result"]["code"])


class TestFirstReadNews(unittest.TestCase):
    auth = ""
    def test_first_readNews(self):
        response = readNews(self.auth)
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        #self.assertTrue(result["Result"]["success"])
        self.assertEqual(True,result["Result"]["success"])
        detail = result["Result"]["detail"]
        firstRead = "noobread" in detail.keys()
        self.assertTrue(firstRead)
    

class TestReadNews(unittest.TestCase):
    auth = ""
    def test_daily_readNews(self):
        response = readNews(self.auth)
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        self.assertEqual(True,result["Result"]["success"])
        detail = result["Result"]["detail"]
        firstRead = "noobread" in detail.keys()
        self.assertFalse(firstRead)


class TestSignIn(unittest.TestCase):
    auth = ""

    def test_AsignIn(self):
        print("当天首次签到---------------------------")
        response = signIn(self.auth)
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        self.assertTrue(result["Result"]["success"])

    def test_BsignInAgain(self):
        print("当天再次签到---------------------------")
        response = signIn(self.auth)
        result = response.json()
        self.assertFalse(result["Result"]["success"])
        self.assertEqual("Error in module [L50] code [615013100] - already sign-in today",result["Result"]["msg"])


 


class TestFirstShareCnt(unittest.TestCase):
    auth=""
    def test_first_shareNews(self):
        #response = shareCnt(self.auth)
        response = task.complete_task(self.auth,"first-share-news")
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        self.assertTrue(result["success"])
    
'''
class TestShareCnt(unittest.TestCase):
    auth = ""
    def test_daily_share(self):
        response = shareCnt(self.auth,url="https://droinews/1111.com")
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        self.assertTrue(result["Result"]["success"])
        detail = result["Result"]["detail"]
        firstShare = "noobshare" in detail.keys()
        self.assertFalse(firstShare)
'''

class TestBindCard(unittest.TestCase):
    auth = ""

    def test_AwrongCard(self):
        print("输入错误的身份证号码----------------------")
        response = bindCard(self.auth,identitycard="11111111111111111")
        result = response.json()
        print(result)
        self.assertFalse(result["Result"]["success"])
        self.assertEqual("Invalid parameter : request.detail.identitycard",result["Result"]["msg"])

    def test_BindCard(self):
        print("用户实名认证----------------------------")
        response = bindCard(self.auth)
        self.assertEqual(200,response.status_code)
        result = response.json()
        print(result)
        self.assertTrue(result["Result"]["success"])

    def test_CalterRealnameAndCard(self):
        print("一次机会修改身份信息--------------------")
        response = bindCard(self.auth,identitycard="450311197509084907",realname="哈哈")
        result = response.json()
        self.assertTrue(result["Result"]["success"])
        self.assertEqual("450311197509084907",result["Result"]["detail"]["identitycard"])
        self.assertEqual("哈哈",result["Result"]["detail"]["realname"])

    def test_DonlyOneAlterChance(self):
        print("有且只有一次修改机会--------------------")
        response = bindCard(self.auth,realname="哈哈哈")
        result = response.json()
        self.assertFalse(result["Result"]["success"])



class TestChangeUserinfo(unittest.TestCase):
    auth = ""
    #正常修改
    def test_AchangeUserinfo(self):
        print("正常修改用户信息-------------------")
        response = changeUserinfo(self.auth,name="ceshi001",gender=1)
        print(response)
        self.assertEqual(response[0],"ceshi001")
        self.assertEqual(response[1],1)
        self.assertTrue(response[2])

    #用户名过长（超过服务端设置）
    def test_BchangeLongname(self):
        print("修改用户信息时，用户名设置过长----------------------")
        response = changeUserinfo(self.auth,name="ceshi1111111111111111111112222222222222222222222255555555")
        self.assertFalse(response)

    #用户名设置过短（用户名需大于2字符能正常修改）
    def test_CchangeShortname(self):
        print("修改用户信息时，用户名称设置过短-------------------")
        response = changeUserinfo(self.auth,name="1")
        self.assertFalse(response)

    #修改用户头像
    def test_DchangeHead(self):
        print("修改用户头像------------------------------------")
        response = changeUserinfo(self.auth,avatar="http://file02.16sucai.com/d/file/2015/0408/779334da99e40adb587d0ba715eca102.jpg")
        print(response)
        self.assertEqual("http://file02.16sucai.com/d/file/2015/0408/779334da99e40adb587d0ba715eca102.jpg",response[3])



class TestDzpPrize(unittest.TestCase):
    auth = ""

    def test_dzpPrize(self):
        print("大转盘抽奖------------------------------------------")
        singlelogin = self.auth + "ZYK_ac17c4b0bb1d5130bf8e0646ae2b4eb4"
        singleauthMD5 = md5Encode(singlelogin.encode("UTF-8"))
        response = Prize(self.auth,singleauthMD5)
        print(response.json())
        self.assertEqual(0,response.json()["result"])
        '''
        try:
            self.assertEqual(0,response.json()["result"])
        except AssertionError as e:
            print("failed")
        '''
@unittest.skip("skipping getPhoneIdentifyingcode")
class TestGetPhoneIdentifyingCode(unittest.TestCase):
    phone = ""

    def test_getPhoneIdentifyingCode(self):
        print("获取手机验证码----------------------------------------")
        result = user.get_phoneIdentifingCode(phone)
        print(result.json())
        self.assertTrue(result.json()["Result"]["success"])

        #每个手机号发送都有60秒的冷却时间，并且一小时内只有5次发送配额
        time.sleep(60)
        result = user.get_phoneIdentifingCode(phone)
        print(result.json())
        self.assertTrue(result.json()["Result"]["success"])

        #间隔时间过短
        time.sleep(10)
        result = user.get_phoneIdentifingCode(phone)
        print(result.json())
        self.assertFalse(result.json()["Result"]["success"])



class TestGetMasterNickName(unittest.TestCase):
    auth = ""

    #用户已做过绑定邀请码任务
    def test_getMasterNickName(self):
        print("获取用户师傅昵称-------------------------------------")
        response  = user.get_masterNickName(self.auth)
        self.assertEqual("有料Kjza7a",response)


class TestAddSlaver(unittest.TestCase):
    auth = ""
    invcode = ""
    #新增1个徒弟，检查徒弟数目是否增加

    def test_addSlaver(self):
        print("新增1个徒弟，检查徒弟数目是否正常增加")
        response = user.get_allFriends(self.auth)
        oldtotal = response.json()["Result"]["detail"]["total"]


        slaver = autoPhone.add_slaver(self.invcode)
        print(slaver.json())

        newresponse = user.get_allFriends(self.auth)
        newtotal = newresponse.json()["Result"]["detail"]["total"]
        self.assertEqual(oldtotal+1,newtotal)



class TestSmallGameFeed(unittest.TestCase):
    auth= ""
    def test_samllgame(self):
        print("玩小游戏赚金币---------------------------------")
        response = task.smallGame(self.auth)
        result = response.json()
        print(result)
        self.assertEqual(0,result["code"])
        self.assertLessEqual(result["data"]["data"]["today_coins"],result["data"]["data"]["receivable_coins"])




class TestZuserlogOff(unittest.TestCase):
    auth = ""
    phone = ""
    def test_ZAlogoff(self):
        print("注销用户------------------------------")
        response = userLogoff.userLogOff(self.auth)
        result = response.json()
        print(result)
        self.assertEqual(0,result["code"])
        self.assertEqual("提交成功",result["data"]["desc"])

    def test_ZBlogoffAgain(self):
        print("再次注销用户------------------------------")
        response = userLogoff.userLogOff(self.auth)
        result = response.json()
        print(result)
        self.assertEqual(-500,result["code"])
        self.assertEqual("token invalid",result["data"]["desc"])

    def test_ZClogin(self):
        print("已注销的用户再次登录-----------------------")
        response = user.login(self.phone,"222222")
        self.assertFalse(response["Result"]["success"])
        self.assertEqual("Error in module [L50] code [615010052] - user has logged out",response["Result"]["msg"])

    def test_ZDrecover(self):
        print("解封已注销的账号-------------------------")
        response = recoverLogin.recoverUserLogin(self.phone)
        self.assertTrue(response.json()["success"])



'''
if __name__ == '__main__':
    print("开始测试前，清除账号信息--------------------------------------------------")
    phone = "13615506716"
    deleteAc(phone)

    print("开始登陆---------------------------------------------------------------")
    auth = user.login(phone, "111111")
    userauth = auth[0]
    invcode = auth[1]
    if auth.__len__() == 0:
        print("登陆失败")
    else:
        print("登录成功,token是:" + userauth)
        print("开始执行单元测试--------------------------------------------------------")
        TestUserMethods.auth = userauth
        TestTaskMethods.auth = userauth
        TestBindMaster.auth = userauth
        TestFirstReadNews.auth = userauth
        TestReadNews.auth = userauth
        TestSignIn.auth = userauth
        TestFirstShareCnt.auth = userauth
        #TestShareCnt.auth = userauth
        TestBindCard.auth = userauth
        TestChangeUserinfo.auth = userauth
        TestDzpPrize.auth = userauth
        TestGetPhoneIdentifyingCode.phone = phone
        TestGetMasterNickName.auth = userauth
        TestAddSlaver.auth = userauth
        TestAddSlaver.invcode = invcode
        TestZuserlogOff.auth = userauth
        TestZuserlogOff.phone = phone
        TestSmallGameFeed.auth = userauth
        unittest.main()


'''


