"""
@作者：余宗源
@文件名：create_database.py
@时间：2020/9/17
@文档说明: 存放创建数据库的函数，供上层调用
"""

import mysql_connection as mct


# 数据库建立文件
def create_database():
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 执行创建数据库的语句
    cdsql = "create database houselease"
    cur.execute(cdsql)

    # 关闭调用窗口
    mct.close_conn(conn, cur)
