#coding=utf-8
import pymysql
from dayan.common.logger import Log
class DB:
    log=Log()
    def __init__(self,host='192.168.100.97',port=3306,user='testuser',passwd='123456',db='DaYan_Platform'):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.db=db
        self.con=None
        self.cur=None
    def connectDB(self):
        try:
            self.con=pymysql.connect(host=self.host,
                                     port=self.port,
                                     user=self.user,
                                     passwd=self.passwd,
                                     db=self.db,
                                     charset='gb2312')
        except pymysql.Error as e:
            self.log.error("数据库连接失败%s" %e)
        self.cur=self.con.cursor()

    def excute(self,sql):
        self.connectDB()
        try:
            self.log.info("开始执行sql语句")
            self.log.info("执行语句：%s" % sql)
            self.cur.execute(sql)
            #print(self.cur.fetchall())
            self.con.commit()
        except Exception as e:
            self.log.error("sql语句执行失败%s" %e)
            self.con.close()
        self.con.close()

if __name__=="__main__":
    a=DB()
    a.connectDB()