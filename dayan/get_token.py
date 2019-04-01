#coding=utf-8
import requests
import threading
def get_token():
    s=requests.session()
    #登录前要先请求发送验证码
    url_getcode="http://192.168.45.191//api/dayan/user/login/getVCode/18358331453"
    r=s.get(url_getcode)

    url_login="http://192.168.45.191//api/dayan/user/login"
    data={
        "code": "888888",
        "phoneNumber": "18358331453",
        "registerChannelId": "1075951745682427907",
        "invitationUid": ""
    }

    r=s.post(url_login,json=data)
    return r.headers['token']


