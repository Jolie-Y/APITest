# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
from mainTest import TestUserMethods,TestTaskMethods,TestSmallGameFeed
from deleteAccount import deleteAc
import user


#单个类测试
if __name__ == '__main__':
    print("开始测试前，清除账号信息--------------------------------------------------")
    phone = "13615506715"
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
        suite = unittest.makeSuite(TestUserMethods)
        #unittest.makeSuite
        filename = r"\Users\wangyan\Documents\YOULKK\youliao_unittest\myreport.html"
        with open(filename,"wb") as fp:
            runner = HTMLTestRunner.HTMLTestRunner(fp,title="test",description="this is a test")
            runner.run(suite)
