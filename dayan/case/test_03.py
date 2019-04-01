#coding=utf-8
import unittest
import requests
from dayan.common.get_token import get_token
from ddt import ddt,data

@ddt
class Test_info(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token=get_token()
        cls.headers={"Content-Type":"application/json",
                     "token":cls.token
                     }
    #1是新闻资讯，后面的数据是页码
    def test_news(self):
        """测试新闻"""
        url="http://192.168.45.191//api/dayan/colligate/information/list/1/1"
        r=requests.get(url,headers=self.headers)
        print(r.text)

        #2是活动资讯，后面的数据是页码
    def test_activity(self):
        """测试资讯"""
        url="http://192.168.45.191//api/dayan/colligate/information/list/2/1"
        r=requests.get(url,headers=self.headers)
        print(r.text)

if __name__=="__main__":
    unittest.main()

