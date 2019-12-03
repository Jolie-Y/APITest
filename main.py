#!/usr/bin/python
# -*- coding: utf-8 -*-
import user

auth = user.login()
if auth.__len__() == 0:
    print("登陆失败")
else:
    print("登录成功,token是:" + auth)
