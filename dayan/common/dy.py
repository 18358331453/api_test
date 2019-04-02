#coding=utf-8
from dayan.common.db_test import DB

a=DB()
sql="SELECT * FROM dy_user_info"
b=a.excute(sql)
