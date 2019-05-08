#coding=utf-8
import sys
sys.path.append("D:\py_workspace\DYJR")
import unittest
from HTMLTestRunner import HTMLTestRunner
from dayan.common.send_mail_1 import send_email_qq
import os
import time



def all_case(rule="test*.py"):
    '''加在所有case下面的用例'''
    case_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),'case')
    discover=unittest.defaultTestLoader.discover(
        case_path,
        pattern=rule,
        top_level_dir=None
    )
    return discover

def run_case(case):
    curpath=os.path.dirname(os.path.realpath(__file__))
    reportpath=os.path.join(curpath,'report')
    if not os.path.exists(reportpath):os.mkdir(reportpath)
    report_time=time.strftime("%Y%m%d%H%M%S")
    reportname=report_time+"result.html"
    reportpath=os.path.join(reportpath,reportname)
    fp=open(reportpath,"wb")
    runner=HTMLTestRunner(stream=fp,
                          verbosity=2,
                          title='接口测试生成报告',
                          description='执行情况'
    )
    runner.run(case)
    fp.close()

if __name__=="__main__":
    run_case(all_case())
    send_email_qq()
