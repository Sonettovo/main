#(1) 查询电子工程系（EE）所开课程的课程编号、课程名称及学分数。
SELECT  C#,CNAME,CREDIT
FROM c390
WHERE C# LIKE 'EE%'

(2) 查询未选修课程“CS-01”的女生学号及其已选各课程编号、成绩
SELECT S#,C#,GRADE
FROM sc390
WHERE NOT EXISTS
( SELECT *
FROM sc390
WHERE sc390.S#=s390.S# AND C#='CS-01'
)

SELECT S#,C#,GRADE
FROM S390,SC390
WHERE S390.S# not IN (SELECT S# FROM SC390 WHERE C#='CS-01')
AND S390.S#=SC390.S#

select js909.s#,grade ,c# 
From JSC909 WHEN c# <> 'CS-01' and js909.s# = jsc909.s# and js909.sex='女'；

select s#,grade,c# 
From JSC909 
WHERE c# <> 'CS-01' and s# in 
(SELECT s# 
FROM js909 
WHERE sex = '女')

查询2000年～2001年出生的学生的基本信息。
select * from js909 WHERE bdate>'2000-01-01 00:00:00' and bdate<'2001-1-1 00:00:00'
SELECT *
FROM S390
WHERE S390.BDATE>'2000-0101 00:00:00' AND BDATE<'2001-12-31 23:59:59'

(4) 查询每位学生的学号、学生姓名及其已选修课程的学分总数。
SELECT S#,SNAME,SUM(CREDIT)
FROM S390,SC390
WHERE S390.S#=SC390.C#

(5) 查询选修课程“CS-02”的学生中成绩第二高的学生学号。
SELECT s# FROM jsc909 WHERE c#='CS-02'and grade =
(SELECT max(grade) FROM jsc909 WHERE c#='CS-02' AND grade < (SELECT MAX(grade)  FROM jsc909 WHERE c#='CS-02'))


SELECT S#
FROM SC390
WHERE C#='CS-02' AND GRADE=
(SELECT MAX(GRADE)
FROM SC390
WHERE C#='CS-02' AND GRADE<(SELECT MAX(GRADE) FROM SC390 WHERE C#='CS-02'))

select `s#` from jsj52_sc047 where `c#`='CS-01' order by grade desc limit 1 offset 1;
SELECT S#
FROM SC390
WHERE C#='CS-01' ORDER BY GRADE DESC LIMIT 1 OFFSET 1

(6) 查询平均成绩超过“王涛“同学的学生学号、姓名和平均成绩，并按学号进行降序排列。
select sc.`s#`,sname,avg(grade) from jsj52_sc047 sc,jsj52_s047 s where sc.`s#`=s.`s#` group by sc.`s#` 
having avg(grade)>(select avg(grade) from jsj52_sc047,jsj52_s047 
where jsj52_sc047.`s#`=jsj52_s047.`s#` and jsj52_s047.sname='王涛') order by sc.`s#` desc;

SELECT S#,SNAME,AVG(GRADE)
FROM SC390,S390
WHERE SC390.S#=S390.S#
GROUP BY SC390.S#
HAVING AVG(GRADE)>(
SELECT AVG(GRADE)
FROM SC390,C390
WHERE SC390.S#=C390.S# AND S390.SNAME='王涛'
ORDER BY SC390.S# DESC

(7)查询选修了计算机专业全部课程（课程编号为“CS-××”）的学生姓名及已获得的学分总数。
SELECT SNAME,SUM(IF(GRADE<60,0,CREDIT))
FROM S390,SC390.C390
WHERE S390.S#=SC390.S# AND C390.C#=SC390.C#
GROUP BY S390.S#
HAVING COUNT(C390.C# LIKE 'CS')=4
ORDER BY S390.S#

SELECT SNAME,SUM(CREDIT)
FROM S390,SC390,C390
WHERE S390.S#=SC390.S# AND C390.C#=SC390.C#
GROUP BY S390.S#
HAVING COUNT(C390.C# LIKE 'CS')=COUNT(
SELECT C#
FROM C390 C
WHERE C# LIKE 'CS'
)
ORDER BY S390.S#


SELECT tmp.sno,sum(if(tmp.grade>=60,tmp.credit,0)) FROM (SELECT sno,sc.cno,credit,grade FROM sc,course WHERE sc.Cno=course.Cno) tmp GROUP BY tmp.sno HAVING COUNT(*)>=3  ORDER BY Sno;
(8) 查询选修了3门以上课程（包括3门）的学生中平均成绩最高的同学学号及姓名
SELECT S390.S#,SNAME
FROM S390,SC390
WHERE S390.S#=SC390.S# AND S# = (
SELECT S390.S#
FROM SC390,S390
WHERE SC390.S#=S390.S#
GROUP BY S390.S#
HAVING BY COUNT(*)>=3
ORDER BY AVG(GRADE) DESC LIMIT 1
)
2．分别在S×××和C×××表中加入记录
(‘01032005’，‘刘竞’，‘男’，‘1993-12-10’，1.75，‘东14舍312’)及(‘CS-03’，“离散数学”，64，4，‘陈建明’)。
insert into jsj52_s047(`s#`,sname,sex,bdate,height,dorm) values('01032005','刘竞','男','1993-12-10',1.75,'东14舍312’);'

INSERT INTO S390(S#,SNAME,SEX,BDATE,HEIGHT,DORM)VALUES('01032005','刘竞','男','1993-12-10',1.75,'东14舍312')；
INSERT INTO C390(C#,CNAME,PERIOD,CREDIT,TEACHER)VALUES('CS-03','离散数学',64,4,'陈建明');

3．将S×××表中已修学分数大于60的学生记录删除。
DELETE FROM S390
WHERE S# IN (
SELECT S390.S#
FROM S390,SC390,C390
WHERE S390.S#=SC390.S# AND C390.C#=SC390.C#
GROUP BY S390.S#
HAVING SUM(CREDIT)>60
);

delete from jsj52_s047 where sname in (select sname from jsj52_s047 s,jsj52_sc047 sc,jsj52_c047 c  
where sc.`s#`=s.`s#` and sc.`c#`=c.`c#`  group by sc.`s#` having sum(credit)>60);

SELECT SNAME,SUM(CASE WHEN GRADE>=60 THEN CREDIT ELSE 0 END)
FROM S390,SC390,C390
WHERE S390.S#=SC390.S# AND C390.C#=SC390.C#
GROUP BY S390.S#
HAVING COUNT(C390.C# LIKE 'CS')=4
ORDER BY S390.S#

4．将“张明”老师负责的“信号与系统”课程的学时数调整为64，同时增加一个学分。
UPDATE C390
SET CREDIT=CREDIT+1,PERIOD=64
WHERE CNAME='信号与系统' AND TEACHER='张明'

5．建立如下视图：
(1)居住在“东18舍”的男生视图，包括学号、姓名、出生日期、身高等属性。
(2)“张明”老师所开设课程情况的视图，包括课程编号、课程名称、平均成绩等属性。
(3)所有选修了“人工智能”课程的学生视图，包括学号、姓名、成绩等属性。
CREATE VIEW S_DORM
AS SELECT S#,SNAME,BDATE,HEIGHT
FROM S390
WHERE SEX='男' AND DORM LIKE '东18舍'
WITH CHECK OPTION

create view sview as select `s#`,sname,bdate,height,dorm from jsj52_s047 where dorm regexp '东八舍*’;'

(2)“张明”老师所开设课程情况的视图，包括课程编号、课程名称、平均成绩等属性。
create view teacher_view as select sc.`c#`,cname,avg(grade) from jsj52_sc047 sc,jsj52_c047 c 
where sc.`c#`=c.`c#` and teacher='张明' group by sc.`c#`;

SELECT C390.C#,CNAME,AVG(GRADE)
FROM C390,SC390
WHERE C390.C#=SC390.C# AND TEACHER='张明'
GROUP BY C390.C#

(3)所有选修了“人工智能”课程的学生视图，包括学号、姓名、成绩等属性。
SELECT s390.S#,SNAME,GRADE
FROM S390,C390,SC390
WHERE S390.S#=SC390.S# AND C390.C#=SC390.C#
AND CNAME='人工智能'

SELECT SNAME,SUM(CASE WHEN GRADE>=60 THEN CREDIT ELSE 0 END)
FROM S390,SC390,C390
WHERE S390.S#=SC390.S# AND C390.C#=SC390.C#
GROUP BY S390.S#
HAVING COUNT(C390.C# LIKE 'CS%')=(
SELECT COUNT(C390.C# LIKE 'CS%')
FROM C390
)
ORDER BY S390.S#




