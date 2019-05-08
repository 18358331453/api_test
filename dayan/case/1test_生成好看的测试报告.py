#coding=utf-8
import unittest
import requests
import time
from ddt import ddt,data
from qlfin_login.get_md5 import get_md5
datas=[{"user":'','passwd':'a111111','return_text':'登录名不能为空'},
       {"user":'13601230662','passwd':'','return_text':'登录失败'},
       {"user":'13601230661','passwd':'a222222','return_text':'登录失败'},
       {"user":'18358331453','passwd':'yanghong1994','return_text':'交易成功'},]
@ddt
class Test_login_ddt(unittest.TestCase):

    def setUp(self):
        self.now_time=time.strftime('%Y%m%d%H%M%S',time.localtime())
        self.url='https://www.qlfin.com/eps/appService/direct.htm'

    def tearDown(self):
        pass
    @data(*datas)
    def test_login_3(self,value):
        """测试数据：{0}"""
        self.data={
            "reqHead":
                {
                    "functionId":"A011",
                    "terminalType":"3",
                    "terminalId":"",
                    "transTime":"",
                    "version":"1.0.0"
                },
            "body":
                {
                    "loginId":value['user'],
                    "password":get_md5(value['passwd']),
                    "type":"0"
                }
        }
        r=requests.post(self.url,json=self.data)
        print(r.text)
        if value['user'] == "13601230660":
            self.assertEqual(r.json()["respHead"]["respMsg"],value['return_text'])
        elif value['user'] == "":
            self.assertEqual(r.json()["respHead"]["respMsg"],value['return_text'])
        else:
            self.assertEqual(r.json()["respHead"]["respMsg"],value['return_text'])

if __name__ == '__main__':
    unittest.main()


