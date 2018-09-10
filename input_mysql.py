# encoding=utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect("183.131.202.162", "root", "Huawei!123", "crawler", charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# SQL 查询语句
sql = "SELECT * FROM ceshi LIMIT 0,200"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    title = []
    content = []
    for row in results:
        title.append(row[1])
        content.append(row[5])
    # 打印结果
    # print("title[0]=%s,content[0]=%s" % (title[0], content[0]))
except:
    print("Error: unable to fetch data")
# 关闭数据库连接
db.close()
