#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import user
import task


class TestUserMethods(unittest.TestCase):
    auth = ""

    def test_get_user_info(self):
        response = user.get_user_info(auth)
        self.assertEqual(200, response.status_code)
        json = response.json()
        self.assertEqual(auth, json['Result']['detail']['auth'])


class TestTaskMethods(unittest.TestCase):
    auth = ""

    def test_get_task_list(self):
        response = task.get_task_list(self.auth)
        self.assertEqual(200, response.status_code)
        json = response.json()
        print(json)
        self.assertTrue(json['success'])

    def test_complete_task(self):
        response = task.complete_task(self.auth, 'dzp-video')
        self.assertEqual(200, response.status_code)
        json = response.json()
        print(json)
        self.assertTrue(json['success'])


if __name__ == '__main__':
    print("开始登陆---------------------------------------------------------------")
    auth = user.login('13333333333', "111111")
    if auth.__len__() == 0:
        print("登陆失败")
    else:
        print("登录成功,token是:" + auth)
        print("开始执行单元测试--------------------------------------------------------")
        TestUserMethods.auth = auth
        TestTaskMethods.auth = auth
        unittest.main()
