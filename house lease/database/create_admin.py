"""
@作者：余宗源
@文件名：create_admin.py
@时间：2020/9/17
@文档说明: 存放创建admin表的函数，供上层调用
"""

import mysql_connection as mct


# 创建admin表,管理员信息表
def createadmin():
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 执行创建表的语句
    clsql = ("create table houselease.admin( "
             "adminID      int primary key,"
             "AdUserName   varchar(255),"
             "AdPassword   date );")
    cur.execute(clsql)

    # 关闭调用
    mct.close_conn(conn, cur)
