import pymysql
class DBHelper:
    # 构造函数
    def __init__(self, host='192.168.100.97', user='testuser',
                 pwd='123456', db='DaYan_Welfare'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None
        self.cur = None
    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(self.host, self.user,
                                        self.pwd, self.db,charset='utf8')
        except pymysql.Error as e:
            print(e)
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None):
        # 连接数据库
        self.connectDatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql, params)
                self.conn.commit()
        except Exception as e:
            print(e)
            self.close()
            return False
        return True

    # 用来查询表数据
    def fetchall(self, sql, params=None):
        self.execute(sql,params)
        return self.cur.fetchall()

if __name__ == '__main__':
    dbhelper = DBHelper()
    dbhelper.connectDatabase()