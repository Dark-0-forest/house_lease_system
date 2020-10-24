"""
@作者：余宗源
@文件名：create_tenant.py
@时间：2020/9/17
@文档说明: 存放创建tenant表的函数，供上层调用
"""

import mysql_connection as mct


# 创建tenant表,租户信息表
def createtenant():
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 执行创建表的语句
    clsql = ("create table houselease.tenant( "
             "tenantID       int primary key AUTO_INCREMENT,"
             "tenantName     varchar(255),"
             "tenantAddress  varchar(255),"
             "TphoneNum      varchar(20),"
             "birthDate      date,"
             "gender         varchar(10),"
             "TUserName      varchar(255),"
             "TPassword      varchar(255) );")
    cur.execute(clsql)
    # 自增变量初始化(其中20表示20年，3表示租客，000表示自增编号)
    aisql = "alter table houselease.tenant AUTO_INCREMENT=203000;"
    cur.execute(aisql)

    # 关闭调用
    mct.close_conn(conn, cur)
