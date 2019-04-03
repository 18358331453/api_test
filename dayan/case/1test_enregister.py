#coding=utf-8
import unittest
import requests
from dayan.common.login import get_headers
from dayan.common.db_test import DB
import warnings
import time
from dayan.common.logger import Log
class Test_enregister(unittest.TestCase):
    log=Log()
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)#忽略警告
        cls.log.info("开始测试前的账号登陆准备")
        cls.headers=get_headers(telphone=18358338888)
        cls.log.info("登陆成功，使用账号：18358338888")
        cls.url='http://192.168.100.142//api/dayan/project/enregister/ope'

    def test_1_enregister(self):
        """支持拼图的，立即登记"""
        data={
            "productId":"21",
            "enregisterShare":"10",
            "isAutoSurvival":"2"
            }
        self.log.info("开始执行登记非拼团操作，使用数据%s" %data)
        r=requests.post(self.url,json=data,headers=self.headers)
        self.log.info("登记非拼团操作状态码%d,返回数据为%s" % (r.status_code,r.text))
        self.assertEqual(r.status_code,200,"请求异常，检查服务状态")
        self.log.info("接口请求成功，状态码200")
        self.log.info("开始校验登记结果")
        self.assertEqual(r.json()['message'],"请求成功","登记结果与预期结果不同")
        self.log.info("登记非拼团操作成功")

    def test_2_enregister_together(self):
        """支持拼图的，拼团登记"""
        data={
            "productId":"21",
            "enregisterShare":"20",
            "togetherId": "1113317082612793346",
            "isAutoSurvival":"2"
        }
        self.log.info("开始执行登记拼团操作，使用数据%s" %data)
        r=requests.post(self.url,json=data,headers=self.headers)
        self.log.info("登记拼团操作状态码:%d,返回数据为%s" % (r.status_code,r.text))
        self.assertEqual(r.status_code,200,"请求异常，检查服务状态")
        self.log.info("接口请求成功")
        self.assertEqual(r.json()['message'],"请求成功","登记结果与预期结果不同")
        self.log.info("登记拼团操作成功")

    def tearDown(self):
        #登记后清除数据
        # time.sleep(30)
        self.log.info("开始执行数据库连接操作")
        self.db=DB()
        delete_enregister_info_sql="DELETE FROM dy_project_product_enregister_info WHERE user_phone_show='183****8888'"
        delete_enregister_together_info_sql="DELETE FROM dy_project_product_enregister_together_info WHERE originator_phone_show='183****8888'"
        delete_message_info_sql="DELETE from dy_instation_message WHERE uid='1113280649072508930' AND title='产品登记'"
        updata_together_num="UPDATE dy_project_product_enregister_together_info SET `now_togethe_num`=1 WHERE `together_id` = 1113317082612793346"
        self.db.excute(sql=delete_enregister_info_sql)
        self.db.excute(sql=delete_enregister_together_info_sql)
        self.db.excute(sql=updata_together_num)
        self.db.excute(sql=delete_message_info_sql)
        self.log.info("关闭数据库连接")
        self.log.info("===================================================================================")
if __name__=="__main__":
    unittest.main()