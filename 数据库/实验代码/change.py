import csv
filepath=''
with open('C:/Users/86199/Desktop/allcourse.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    result=list(reader)
    i=1#开始行数
    headc2=['C#','CNAME','TEACHER','PERIOD','CREDIT']
    new_filepath1='C:/Users/86199/Desktop/new_allcourse.csv'#新文件存储路径
    with open(new_filepath1, "w", newline='') as f:
        f.truncate()
        writer = csv.writer(f)
        writer.writerow(headc2)#只打印一次
    while True:
        Cnumber=result[i][0]
        old_Cnumber=result[i+1][0]
        if old_Cnumber==Cnumber:
            print('舍去列：',result[i])
        else:
            row=result[i]
            with open(new_filepath1, "a+", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(row)
        i=i+1
        try:
            a=result[i+1]
        except Exception as e:
            print("完成：\n",e)