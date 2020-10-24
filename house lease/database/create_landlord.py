"""
@作者：余宗源
@文件名：create_landlord.py
@时间：2020/9/17
@文档说明: 存放创建landlord表的函数，供上层调用
"""

import mysql_connection as mct


# 创建landlord表,房主信息表
def createlandlord():
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 执行创建表的语句
    clsql = ("create table houselease.landlord( "
             "landlordID      int primary key AUTO_INCREMENT,"
             "landlordName    varchar(255),"
             "landlordAddress varchar(255),"
             "LphoneNum       varchar(20),"
             "LUserName       varchar(255) not null,"
             "LPassword       varchar(255) not null );")
    cur.execute(clsql)
    # 自增变量初始化(其中20表示20年，1表示房主，000表示自增编号)
    aisql = "alter table houselease.landlord AUTO_INCREMENT=201000;"
    cur.execute(aisql)

    # 关闭调用
    mct.close_conn(conn, cur)
