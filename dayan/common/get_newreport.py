#coding=utf-8
import os

def get_report_file():
    report_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    report_path=os.path.join(report_path,'report')
    lists=list(os.listdir(report_path))
    lists.sort(key=lambda x:os.path.getmtime(os.path.join(report_path,x)))
    report_file=os.path.join(report_path,lists[-1])
    # print(report_file)
    return report_file
# get_report_file()