#coding=utf-8
import requests
from dayan.common.get_token import get_token
from dayan import 获取token并写入yaml as e
headers={"Content-Type":"application/json",
         "token":get_token()
         }

url_getinfo="http://192.168.45.191//api/dayan/user/relevant/info"
try:
    r=requests.get(url_getinfo,headers=headers)
    assert r.json()['data']['headImgUrl'] == None
except KeyError:
    e.write_yaml(e.get_token())
    r=requests.get(url_getinfo,headers=headers)
    headers['token']=get_token()
    print("token已过期，重新执行")
else:
    print(r.text)
    assert r.json()['data']['headImgUrl'] == None
