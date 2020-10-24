"""
@作者：余宗源
@文件名：create_viewing.py
@时间：2020/9/17
@文档说明: 存放创建viewing表的函数，供上层调用
"""

import mysql_connection as mct


# 创建viewing表，看房信息表
def createviewing():
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 执行创建表的语句
    clsql = ("create table houselease.viewing( "
             "viewingID     int primary key AUTO_INCREMENT,"
             "tenantID      int,"
             "houseID       int,"
             "tenantName    varchar(255),"
             "houseAddress  varchar(255),"
             "charge        float,"       
             "viewDate      date);")
    cur.execute(clsql)
    # 自增变量初始化(其中20表示20年，4表示看房记录，000表示自增编号)
    aisql = "alter table houselease.viewing AUTO_INCREMENT=204000;"
    cur.execute(aisql)

    # 关闭调用
    mct.close_conn(conn, cur)
