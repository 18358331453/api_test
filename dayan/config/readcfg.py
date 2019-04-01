#coding=utf-8

import os
import configparser

cur_path=os.path.dirname(os.path.realpath(__file__))
cfg_path=os.path.join(cur_path,'cfg.ini')
conf=configparser.ConfigParser()
conf.read(cfg_path,encoding='utf-8')
smtp_server=conf.get('email','smtp_server')
port=conf.get('email','port')
sender=conf.get('email','sender')
psw=conf.get('email','psw')
receiver=conf.get('email','receiver')
