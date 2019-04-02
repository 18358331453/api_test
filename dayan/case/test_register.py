#coding=utf-8
import unittest
import requests
from dayan.common.db_test import DB
from dayan.common.login import get_headers
import warnings
import time
from dayan.common.logger import Log

class Test_register(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log=Log()
        warnings.simplefilter('ignore', ResourceWarning)
        #删除该用户注册数据
        cls.log.info("开始执行数据清理操作")
        cls.ope_db=DB()
        cls.sql="DELETE FROM dy_user_info WHERE `phone_show`='183****3333'"
        cls.ope_db.excute(cls.sql)
        cls.log.info("数据清理完成")
        time.sleep(10)
        cls.url_shiming_message='http://192.168.100.142//api/dayan/user/realAuth/sendVerificationCode/18358333333'
        cls.url_submit_shiming='http://192.168.100.142//api/dayan/user/realAuth/ope'
        cls.url_pingce='http://192.168.100.142//api/dayan/user/riskAssessment/ope/100'
    def setUp(self):
        self.s=requests.session()
        self.log.info("开始执行用户注册操作，注册用户为18358333333")
        self.headers=get_headers(18358333333)
        self.log.info("开始执行用户注册操作，注册用户为18358333333")

    def test_register(self):
        #获取实名验证码
        # time.sleep(10)
        self.log.info("开始获取实名短信验证码")
        r=self.s.get(self.url_shiming_message,headers=self.headers)
        self.assertEqual(r.json()['message'],'请求成功',msg="实名验证码获取短信验证码异常")
        self.log.info("获取实名短信验证码成功")
        data={
            "name": "自动实名",
            "phone": "18358333333",
            "identityNum": "420000198506204962",
            "bankAccount": "6212261204000463333",
            "verificationCode": "888888",
            "bankAlias": "ICBC",
            "bankName": "工商银行",
            "bankBranch":"工商银行杭州分行"
        }
        #提交实名
        self.log.info("开始进行实名操作")
        r=self.s.post(self.url_submit_shiming,headers=self.headers,json=data)
        self.assertEqual(r.json()['message'],'请求成功',msg="提交实名操作异常")
        self.log.info("实名认证操作成功")

        #提交风险评测
        data={"score":"100"}
        self.log.info("开始进行风险评测操作")
        r=self.s.post(self.url_pingce,headers=self.headers,data=data)
        self.assertEqual(r.json()['message'],'请求成功',msg="评测操作异常")
        self.assertEqual(r.json()['data'],'进取型',msg="评测结果操作异常")
        self.log.info("风险评测操作成功，结果为：%s" % r.json()['data'])


    @classmethod
    def tearDownClass(cls):
        pass
if __name__=="__main__":
    unittest.main()