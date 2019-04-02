#coding=utf-8
import pymysql

class DB:
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
            print(e)
        self.cur=self.con.cursor()

    def excute(self,sql):
        self.connectDB()
        try:
            self.cur.execute(sql)
            print(self.cur.fetchall())
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.close()
        self.con.close()

if __name__=="__main__":
    a=DB()
    a.connectDB()