#coding=utf-8
import requests
from dayan.common.logger import Log
import unittest
import warnings
class Test_login(unittest.TestCase):
    log=Log()
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.s=requests.session()

    def test_login(self,phone='18358332002'):
        #登录前要先请求发送验证码
        self.url_getcode="http://192.168.45.191//api/dayan/user/login/getVCode/"+phone
        self.log.info('开始登录前获取验证码操作,使用手机号%s' % phone)
        r=self.s.get(self.url_getcode)
        # self.assertEqual(r.json()['message'],'请求成功142242242')
        # try:
        #     self.assertEqual(r.json()['message'],'请求成功142242')
        #     result=10/0
        # except Exception:
        #     self.log.error('登录失败')
        self.log.info('获取验证码操作结果%s'% r.json())
        self.log.info('获取是否获取验证码成功:%s'% r.json()['message'])
        self.assertEqual(r.json()['message'],'请求成功')
        #登录操作
        self.url_login="http://192.168.45.191//api/dayan/user/login"
        data={
        "code": "888888",
        "phoneNumber":phone,
        "registerChannelId": "",
        "invitationUid": ""
        }
        self.log.info('开始执行登录操作')
        r=self.s.post(self.url_login,json=data)
        self.log.info('获取是否登录成功结果:%s'% r.json()['message'])
        self.assertEqual(r.json()['message'],'请求成功')
        self.log.info('获取登录成功之后的token:%s'% r.headers['token'])


if __name__== "__main__":
    unittest.main()