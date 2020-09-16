# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
from mainTest import TestAddSlaver,TestBindCard,TestBindMaster,TestChangeUserinfo,TestDzpPrize,TestFirstReadNews,TestFirstShareCnt,TestGetMasterNickName,TestGetPhoneIdentifyingCode,TestReadNews,TestSignIn,TestSmallGameFeed,TestTaskMethods,TestUserMethods,TestZuserlogOff
from deleteAccount import deleteAc
import user
import time

def runTest():
    
    print("开始测试前，清除账号信息--------------------------------------------------")
    phone = "13819593118"
    #deleteAc(phone)

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





        #suite = unittest.makeSuite(TestUserMethods)
        #unittest.makeSuite
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        
        suite.addTest(loader.loadTestsFromTestCase(TestSmallGameFeed))
        suite.addTest(loader.loadTestsFromTestCase(TestTaskMethods))
        suite.addTest(loader.loadTestsFromTestCase(TestUserMethods))
        suite.addTest(loader.loadTestsFromTestCase(TestBindMaster))

        suite.addTest(loader.loadTestsFromTestCase(TestFirstReadNews))
        suite.addTest(loader.loadTestsFromTestCase(TestReadNews))
        suite.addTest(loader.loadTestsFromTestCase(TestSignIn))
        suite.addTest(loader.loadTestsFromTestCase(TestFirstShareCnt))
        #suite.addTest(loader.loadTestsFromTestCase(TestShareCnt))
        suite.addTest(loader.loadTestsFromTestCase(TestBindCard))
        suite.addTest(loader.loadTestsFromTestCase(TestChangeUserinfo))
        suite.addTest(loader.loadTestsFromTestCase(TestDzpPrize))

        suite.addTest(loader.loadTestsFromTestCase(TestGetPhoneIdentifyingCode))
        suite.addTest(loader.loadTestsFromTestCase(TestGetMasterNickName))
        suite.addTest(loader.loadTestsFromTestCase(TestAddSlaver))
        suite.addTest(loader.loadTestsFromTestCase(TestZuserlogOff))


        

        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        #filename = r"\Users\wangyan\Documents\YOULKK\youliao_unittest\myreport1.html"
        filename = r"\Users\wangyan\Documents\YOULKK\youliao_unittest\myreport_"+now+".html"
        with open(filename,"wb") as fp:
            runner = HTMLTestRunner.HTMLTestRunner(fp,title="test",description="有料任务接口测试")
            runner.run(suite)


if __name__ == '__main__':
    runTest()
