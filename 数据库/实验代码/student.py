# coding : UTF-8
#python随机生成学生数据
import csv
from datetime import date
import math
from faker import Faker # 导入Faker
faker = Faker()
# 中文需要使用zh_CN
fake = Faker('zh_CN')
i=0
Snum=[]
while i<1000:
    #Snumber,SNAME,SEX,BDATE,HEIGHT,DORM
    louhao=i//500+2#从东/西2舍开始住
    susehao=i//4%500+101#宿舍号100-600；4个人一个宿舍
    if i%2==1:
        Sname=fake.name_male()#生成男生姓名
        SEX='男'
        Snumber='0'+str(i+2000000)#0200 0000--0200 0000
        HEIGHT=fake.random_int(min=160,max=190)*0.01
        DORM='东'+str(louhao)+'舍'+str(susehao)
    else:
        Sname=fake.name_female()#女生
        SEX='女'
        Snumber='0'+str(i+2200000)#0220 0000--0220 9999
        HEIGHT=fake.random_int(min=150,max=180)*0.01
        DORM='西'+str(louhao)+'舍'+str(susehao)
#    HEIGHT=round(HEIGHT,2)
    HEIGHT=format(HEIGHT, '.2f')
    BDATE=fake.date_between(start_date=date(2001,1,1),end_date=date(2003,12,31))
    print(Snumber,Sname,SEX,BDATE,HEIGHT,DORM)
    i=i+1
    headc=['S#','SNAME','SEX','BDATE','HEIGHT','DORM']
    Clist=[Snumber,Sname,SEX,BDATE,HEIGHT,DORM]
    #create sc390_1
    Ccount=fake.random_int(min=1,max=9)#选修的科目数
    Record=[]
    x=0
    count2=0
    for x in range(Ccount):
        count1=fake.random_int(min=1,max=190)#选修的科目序号
        if x>0:
            while True:
                for check in Record:
                    if count1==check:
                        count2=1
                if count2==1:
                    count1=fake.random_int(min=1,max=190)
                    count2=0
                    continue
                else:
                    break
        Record.append(count1)
        print(Record)
        with open('C:/Users/86199/Desktop/new_course.csv','r') as csvfile:
            reader = csv.reader(csvfile)
            result=list(reader)
            rows=result[count1]
            Snum.append(rows[0])
            GRADE=fake.random_int(min=0,max=100)
            GRADE=int(math.sqrt(GRADE)*10)
            SClist=[Snumber,rows[0],GRADE] 
            filepath1='C:/Users/86199/Desktop/sc.csv'
            with open(filepath1,"a+",newline='') as f:
                writer1=csv.writer(f)
                writer1.writerow(SClist)
    filepath='C:/Users/86199/Desktop/student.csv'#csv文件存储路径
    with open(filepath, "a+", newline='') as f:
        writer = csv.writer(f)
        if i==1:
            writer.writerow(headc)
        writer.writerow(Clist)    