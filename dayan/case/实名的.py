#coding=utf-8
from dayan.common.login import get_headers
import requests

def shiming(telphone):
    #登录并获取登录后的token
    headers=get_headers(telphone)
    url="http://192.168.45.191//api/dayan/user/realAuth/ope"
    s=requests.session()
    #先获取验证码
    url_yzm="http://192.168.45.191//api/dayan/user/realAuth/sendVerificationCode/"+str(telphone)
    r=requests.get(url_yzm,headers=headers)

    data={
        "name": "杨洪",
        "phone": str(telphone),
        "identityNum": "330382199408167153",
        "bankAccount": "62122612040004767503",
        "verificationCode": "888888",
        "bankAlias": "ICBC",
        "bankName": "工商银行",
        "bankBranch":"支行名称"
    }
    s=s.post(url,json=data,headers=headers)
    print(s.text)

if __name__=="__main__":
    shiming(18358331453)
