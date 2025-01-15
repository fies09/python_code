#coding = utf-8
'''
    标题  删除语句
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
    #3,执行sql语句
    res = cur.execute("delete from tb_movie where `rank` = 1")
    print(res)
   #提交事物
    con.commit()
    print(">>事物提交成功!")
except:
    #事物回退
    con.rollback()
    print('>>事物回退成功!')
#4.关闭数据库
cur.close()
con.close()