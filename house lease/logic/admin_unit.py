"""
@作者：余宗源
@文件名：admin_unit.py
@时间：2020/9/18
@文档说明: 完成关于管理员信息的查询，并将其封装为函数，为用户登录提供接口
"""

import mysql_connection as mct


# 在表中查询登录信息
def admin_login(ae):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据用户名和密码进行查询
    sql = "select * from houselease.admin where AdUserName = %s and AdPassword = %s"
    cur.execute(sql, (ae.getauname(), ae.getapwd()))
    data = cur.fetchone()

    return data