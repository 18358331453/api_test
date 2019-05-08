#coding=utf-8
import unittest
import requests
from dayan.common.db_test import DB
from dayan.common.login import get_headers
import warnings
from dayan.common.logger import Log
from ddt import ddt,data
import time
@ddt
class Test_register(unittest.TestCase):
    log=Log()
    def setUp(self):
        print("setup")
        warnings.simplefilter('ignore', ResourceWarning)
        self.url_shiming_message='http://192.168.100.142//api/dayan/user/realAuth/sendVerificationCode/18358333333'
        self.url_submit_shiming='http://192.168.100.142//api/dayan/user/realAuth/ope'
        self.url_pingce='http://192.168.100.142//api/dayan/user/riskAssessment/ope/100'
        # self.s=requests.session()
        self.headers=get_headers(18358333333)
        # token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIxMTEzNjQ4MDczMzYxODgzMTM3IiwiaXNzIjoiZGF5YW4iLCJleHAiOjE1NTQ1MjIxNjUsIl8iOjE1NTQzNDkzNjU5NTd9.2713Jo86QuCoIMePGfuUWyBjnW-N7gvYxZea4Eu-eso"
        # self.headers={"Content-Type":"application/json",
        #          "token":token
        # }
    data1=[#{"name": "自动实名","phone": "18358333333","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"正常场景"},
               {"name": "","phone": "18358333333","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"姓名为空"},
               {"name": "自动实名","phone": "","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"手机号为空"},
               {"name": "自动实名","phone": "18358333333","identityNum": "","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"身份证号码为空"},
               {"name": "自动实名","phone": "18358333333","identityNum": "420000198506204962","bankAccount": "","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"银行卡号为空"},
               {"name": "自动实名","phone": "18358333333","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"短信验证码为空"},
               {"name": "自动实名","phone": "18358333333","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"银行简称为空"},
               {"name": "自动实名","phone": "18358333333","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "","bankBranch":"工商银行杭州分行","casename":"银行名称为空"},
               {"name": "自动实名","phone": "18358333333","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"","casename":"分行名称为空"},
               #{"name": "自动实名","phone": "18358333333","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"数据正常，但不请求发送验证码"}
               ]

    def test_register(self):
        data={"name": "自动实名","phone": "18358332042","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"数据正常，但不请求发送验证码"}
        # if send_data['casename'] == "数据正常，但不请求发送验证码":
        #     print(send_data['casename'])
        #     r=self.s.get(self.url_shiming_message,headers=self.headers)

        data.pop('casename')
        r=requests.post(self.url_submit_shiming,headers=self.headers,json=data)
        print(r.text)




    def tearDown(self):
        # time.sleep(3)
        url="http://192.168.100.142/api/dayan/user/logout"
        requests.get(url,headers=self.headers)
        print("teardown")
        # self.ope_db=DB()
        # self.sql="DELETE FROM dy_user_info WHERE `phone_show`='183****3333'"
        # self.ope_db.excute(self.sql)
        #test
if __name__=="__main__":
    unittest.main()