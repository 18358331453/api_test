#coding=utf-8
import requests

def huikuan():
    url="http://192.168.45.191//api/dayan/admin/welfare/remittance/import/Ope"
    files = {'remittanceExcelFile':(open("C:\\Users\\thinkpad\\Desktop\\1.xlsx", 'rb'))}

    # files = {'remittanceExcelFile':open("C:\\Users\\thinkpad\\Desktop\\1.xlsx", 'rb')}
    # files = {'remittanceExcelFile':('1.xlsx',open("C:\\Users\\thinkpad\\Desktop\\1.xlsx", 'rb'),"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}

    headers={
            # "Content-Type":"multipart/form-data",
             "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIxIiwiaXNzIjoiZGF5YW4iLCJuYW1lIjoi5ZKM5p6XIiwiZXhwIjoxNTUzNzUxNDQ0LCJfIjoxNTUzNTc4NjQ0MTYzfQ.bx-yqfd-JtgrZsv6GARyqA7SEnY2AfBvCFCWayXICYU"
             }
    data={"remittanceExcelFile":files}

    s=requests.post(url,headers=headers,files=files)
    # s=requests.post(url,headers=headers,files=files)
    print(s.text)

if __name__=="__main__":
    huikuan()
