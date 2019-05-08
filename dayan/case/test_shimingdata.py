#coding=utf-8
import unittest
import requests
from dayan.common.db_test import DB
from dayan.common.login import get_headers
import warnings
from ddt import ddt,data
from dayan.common.logger import Log
import time

@ddt
class Test_register(unittest.TestCase):
    log=Log()
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        for i in range(11):
            self.sql="DELETE FROM dy_user_info WHERE `phone_show`='183****333%d'" % i
            self.ope_db.excute(self.sql)
        self.url_shiming_message='http://192.168.100.142//api/dayan/user/realAuth/sendVerificationCode/18358333333'
        self.url_submit_shiming='http://192.168.100.142//api/dayan/user/realAuth/ope'
        self.url_pingce='http://192.168.100.142//api/dayan/user/riskAssessment/ope/100'

    data1=[{"name": "自动实名","phone": "18358333330","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"正常场景"},
          {"name": "","phone": "18358333331","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"姓名为空"},
          {"name": "自动实名","phone": "","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"手机号为空"},
          {"name": "自动实名","phone": "18358333332","identityNum": "","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"身份证号码为空"},
          {"name": "自动实名","phone": "18358333333","identityNum": "420000198506204962","bankAccount": "","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"银行卡号为空"},
          {"name": "自动实名","phone": "18358333334","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"短信验证码为空"},
          {"name": "自动实名","phone": "18358333335","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"银行简称为空"},
          {"name": "自动实名","phone": "18358333336","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "","bankBranch":"工商银行杭州分行","casename":"银行名称为空"},
          {"name": "自动实名","phone": "18358333337","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"","casename":"分行名称为空"},
          {"name": "自动实名","phone": "18358333338","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "888888","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"数据正常，但不请求发送验证码"},
          {"name": "自动实名","phone": "18358333338","identityNum": "420000198506204962","bankAccount": "6212261204000463333","verificationCode": "777777","bankAlias": "ICBC","bankName": "工商银行","bankBranch":"工商银行杭州分行","casename":"验证码错误"}

           ]
    @data(*data1)
    def test_register(self,send_data):
        """本次使用的测试数据为：{0}"""
        self.log.info("本次次数场景为：%s" % send_data['casename'])
        self.s=requests.session()
        self.headers=get_headers(send_data['phone'])
        #获取实名验证码
        # time.sleep(10)
        # if send_data['casename'] != "数据正常，但不请求发送验证码":
        #     print(send_data['casename'])
        #     r=self.s.get(self.url_shiming_message,headers=self.headers)
        # else:
        #     pass
        #提交实名，执行前删除数据中的casename
        send_data.pop('casename')
        r=self.s.post(self.url_submit_shiming,headers=self.headers,json=send_data)
        print(r.text)




    def tearDown(self):
        for i in range(11):
            self.sql="DELETE FROM dy_user_info WHERE `phone_show`='183****333%d'" % i
            self.ope_db.excute(self.sql)


if __name__=="__main__":
    unittest.main()