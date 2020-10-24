"""
@作者：余宗源
@文件名：mysql_connection.py
@时间：2020/9/17
@文档说明: 存放连接mysql的基本函数，供上层调用
"""
import pymysql

# 对参数进行初始化,这是连接到我的云数据库的外网地址和端口以及账号信息
myhost = 'cdb-m0ca7iiw.cd.tencentcdb.com'
myuser = 'root'
mypassword = '252597248a'
myport = 10098
mycharset = 'utf8'


# 创建connection连接
def create_connection():
    try:
        # 建立到云mysql数据库的连接
        connect = pymysql.connect(host=myhost, user=myuser, password=mypassword, port=myport, charset=mycharset)
        return connect

    except pymysql.Error:
        print("数据库连接异常")


# 关闭连接
def close_conn(conn, cursor):
    try:
        # 关闭对数据库的连接
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    except pymysql.Error:
        print("数据库关闭异常")