#coding=utf-8
import requests
import threading


def test_req_01(token):
    requrl='http://192.168.45.191//api/dayan/project/enregister/ope'
    headers={
        "Content-Type":"application/json",
        "token":token
    }
    data={
        "productId":"1",
        "enregisterShare":"10",
        "isAutoSurvival":"2"
    }
    r=requests.post(requrl,json=data,headers=headers)
    print(r.text)
token=input("输入一个token:")
thread=[]
for i in range(3):
    t1=threading.Thread(target=test_req_01,args=(token,))
    thread.append(t1)

if __name__=='__main__':
    for t in thread:
        t.setDaemon(True)
        t.start()

    for t2 in thread:
        t2.join()
    print('所有线程结束')