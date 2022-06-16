# coding : UTF-8
import json
import re
import csv
from time import sleep
# import urllib.request
from bs4 import BeautifulSoup
import requests
url='http://ehall.xjtu.edu.cn/jwapp/sys/kcbcx/*default/index.do?amp_sec_version_=1&gid_=c2NqVzJXSmpFRXpaR0xRK1h1VWs3NzV3Y3E0N1F6SUFoZnByS2ZFTmNNSldSZlpKVHdqL1dXdDg3VVYvUE5LN2hDRy8yQ1VFTEh2QlFnMEtCYjBwUUE9PQ&EMAP_LANG=zh&THEME=cherry#/qxkcb'
ur2='http://ehall.xjtu.edu.cn/jwapp/sys/kcbcx/modules/qxkcb/qxfbkccx.do'
#电子信息学部开设课
data={
    'querySetting': '[{"name":"KKDWDM","caption":"开课单位","linkOpt":"AND","builderList":"cbl_String","builder":"equal","value":"13430000","value_display":"电子与信息学部"},[{"name":"XNXQDM","value":"2021-2022-2","linkOpt":"and","builder":"equal"},[{"name":"RWZTDM","value":"1","linkOpt":"and","builder":"equal"},{"name":"RWZTDM","linkOpt":"or","builder":"isNull"}]],{"name":"*order","value":"+KKDWDM,+KCH,+KXH","linkOpt":"and","builder":"equal"}]',
    '*order': '+KKDWDM,+KCH,+KXH',
    'SKXQ':'' ,
    'KSJC':'', 
    'JSJC': '',
    'pageSize': '267',#爬取课程数
    'pageNumber': '1'
}
#全校课程
data2={
    'querySetting': '[[{"name":"XNXQDM","value":"2021-2022-2","linkOpt":"and","builder":"equal"},[{"name":"RWZTDM","value":"1","linkOpt":"and","builder":"equal"},{"name":"RWZTDM","linkOpt":"or","builder":"isNull"}]],{"name":"*order","value":"+KKDWDM,+KCH,+KXH","linkOpt":"and","builder":"equal"}]',
    '*order': '+KKDWDM,+KCH,+KXH',
    'SKXQ':'' ,
    'KSJC':'', 
    'JSJC': '',
    'pageSize': '10',#爬取课程数
    'pageNumber': '1'
}
headers1={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '416',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'EMAP_LANG=zh; THEME=cherry; _WEU=Y6ffYJmKrqvFgxAwF*SjzWiwvNQf8rv0oy6WevwLjBe7rbpiDN_rd3Cb1xMQI7b0oa9Oij*kvr4aM0FpBtCq07s*w_1u5*YiQyQFEJwhYcP.; _ga=GA1.3.2008857839.1631885259; CASTGC=jx/xidJbMs6V8QxEl50JQQD+zxy0rw1LxLCN4U5ZHxorfnFDKXJVHQ==; MOD_AMP_AUTH=MOD_AMP_8b7ad1bc-05a7-4381-9b9c-a7322c0f61bf; route=ab22dc972e174017d573ee90262bcc96; asessionid=f04cf420-8e2f-4fcd-8251-6c3fbe0cffe6; amp.locale=undefined; JSESSIONID=hGwatNzMsRpB1sQHsEMYc3myszdTmX-A4B6EVM624L5-xKwTgd_F!544624662',
    'Host': 'ehall.xjtu.edu.cn',
    'Origin': 'http://ehall.xjtu.edu.cn',
    'Referer': 'http://ehall.xjtu.edu.cn/jwapp/sys/kcbcx/*default/index.do?amp_sec_version_=1&gid_=c2NqVzJXSmpFRXpaR0xRK1h1VWs3NzV3Y3E0N1F6SUFoZnByS2ZFTmNNSldSZlpKVHdqL1dXdDg3VVYvUE5LN2hDRy8yQ1VFTEh2QlFnMEtCYjBwUUE9PQ&EMAP_LANG=zh&THEME=cherry',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
response=requests.post(ur2,data=data,headers=headers1)
response_dict=json.loads(response.text)
soup1=BeautifulSoup(response.text,'lxml')
#print(soup1)
#解析抓包内容
Cnumber=re.findall('\"KCH\":\"(.*?)\"',str(soup1))#课程号
Cname=re.findall('\"KCM\":\"(.*?)\"',str(soup1))#课程名
TEACHER=re.findall('\"SKJS\":\"(.*?)\"',str(soup1))#教师姓名
PERIOD=re.findall('\"XS\":(.*?),',str(soup1))#学时
#PERIOD2=re.findall('\"SYXS\":(.*?),',str(soup1))#实验课学时
CREDIT=re.findall('\"XF\":(.*?),',str(soup1))#学分
#fp=open()
#print(Cnumber,'\n',Cname,'\n',TEACHER,'\n',PERIOD,'\n',CREDIT)
#写入csv文件
headc=['C#','CNAME','TEACHER','PERIOD','CREDIT']
Clist=zip(Cnumber,Cname,TEACHER,PERIOD,CREDIT)
filepath='C:/Users/86199/Desktop/course.csv'#csv文件存储路径
with open(filepath, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headc)
    for row in Clist:
        writer.writerow(row)

sleep(0.5)

#3910条数据
i=1
while True:
    if i<395:
        data2['pageNumber']=str(i)
        print(data2)
    if i==1000:
        data2['pageNumber']=str(i)
        data2['pageSize']='910'
        print(data2)
    response2=requests.post(ur2,data=data2,headers=headers1)
    response_dict2=json.loads(response2.text)
    soup2=BeautifulSoup(response2.text,'lxml')
#print(soup2)
#解析抓包内容
    Cnumber2=re.findall('\"KCH\":\"(.*?)\"',str(soup2))#课程号
    Cname2=re.findall('\"KCM\":\"(.*?)\"',str(soup2))#课程名
    TEACHER2=re.findall('\"SKJS\":\"(.*?)\"',str(soup2))#教师姓名
    PERIOD2=re.findall('\"XS\":(.*?),',str(soup2))#学时
    #PERIOD2=re.findall('\"SYXS\":(.*?),',str(soup2))#实验课学时
    CREDIT2=re.findall('\"XF\":(.*?),',str(soup2))#学分
#fp=open()
#print(Cnumber2,'\n',Cname2,'\n',TEACHER2,'\n',PERIOD2,'\n',CREDIT2)
#写入csv文件
    headc2=['C#','CNAME','TEACHER','PERIOD','CREDIT']
    Clist=zip(Cnumber2,Cname2,TEACHER2,PERIOD2,CREDIT2)
    filepath='C:/Users/86199/Desktop/allcourse.csv'#csv文件存储路径
    with open(filepath, "a+", newline='') as f:
        writer = csv.writer(f)
        if i==1:
            writer.writerow(headc2)#只打印一次
        for row in Clist:
            writer.writerow(row)
    i=i+1
    if i==395:
        break
#    sleep(0.1)
print('OK!!!!!!!')