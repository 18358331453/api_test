#coding=utf-8
import unittest

class Test_daying(unittest.TestCase):
    def setUp(self):
        pass
    def test_print(self):
        a,b=1,2
        self.assertEqual(3,a+b)
        print("git 提交测试")
if __name__=="__main__":
    unittest.main()