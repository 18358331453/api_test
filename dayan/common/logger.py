#coding=utf-8
import logging,time
import os

#log_path是存放日志的路径
cur_path=os.path.dirname(__file__)
log_path=os.path.join(os.path.dirname(cur_path),'logs')
#如果不存在logs文件夹则创建一个
if not os.path.exists(log_path):os.mkdir(log_path)

class Log():
    def __init__(self):
        #文件的命名
        self.logname=os.path.join(log_path,'%s.log' % (time.strftime('%Y%m%d')))
        self.logger=logging.getLogger(__name__)
        self.logger.setLevel(level=logging.DEBUG)
        #日志输出格式
        self.formatter=logging.Formatter(fmt='%(asctime)s - %(filename)s - %(levelname)s %(message)s')

    def console(self,level,message):
        #创建filehandle，用于写日志到文件
        filehandle=logging.FileHandler(self.logname,encoding='utf-8')
        filehandle.setLevel(level=logging.DEBUG)
        filehandle.formatter=self.formatter
        self.logger.addHandler(filehandle)

        #创建一个控制台输出handle
        streamhanlde=logging.StreamHandler()
        streamhanlde.setLevel(level=logging.DEBUG)
        streamhanlde.formatter=self.formatter
        self.logger.addHandler(streamhanlde)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message,exc_info=True)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(filehandle)
        self.logger.removeHandler(streamhanlde)
    def debug(self,message):
        self.console('debug',message)
    def info(self, message):
        self.console('info', message)

    def warning(self, message):
        self.console('warning', message)

    def error(self, message):
        self.console('error', message)
if __name__ == "__main__":
    log=Log()
    log.info('--测试开始--')
    log.info('操作步骤1,2,3')
    log.warning('----测试结束----')

