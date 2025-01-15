#coding = utf-8
'''
    标题  添加字段
    @name:
    @function:
    @author: Mr.Fan
    @date:2020--  
'''
import pymysql
#1,建立连接
con = pymysql.connect(host='localhost',port=3306,user='root',passwd='fy961009',db='db_movie')
#判断连接状态
if con:
    print(">>数据库连接成功!")
else:
    print(">>数据库连接失败!")
#2,获取游标对象
cur = con.cursor()
# print(cur)
#执行sql语句
#处理异常
try:
    res = cur.execute("insert into tb_movie values(1,'肖申克的救赎'),(2,'霸王别姬')")
    # print(res)
    #提交事物
    con.commit()
    print(">>事物提交成功!")
except:
    #回退事物
    con.rollback()
    print(">>事物回退成功!")
# 关闭数据库
cur.close()
con.close()
