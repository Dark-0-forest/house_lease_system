"""
@作者：余宗源
@文件名：tenant_module.py
@时间：2020/9/18
@文档说明: 完成关于租户信息的一些操作，并将其封装为函数，为上层调用提供接口
"""

import mysql_connection as mct


# 看房记录的插入
def viewing_insert(ve):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 插入看房记录
    sql = "insert into houselease.viewing values(null, %s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (ve.gettid(), ve.gethid(), ve.gettname(), ve.gethaddress(), float(ve.getcharge()), ve.getvdate()))
    conn.commit()

    # 关闭调用
    mct.close_conn(conn, cur)


# 看房记录的查询
def viewing_select(ve):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据条件在viewing表进行查询
    vssql = "select * from houselease.viewing where 1 "
    if ve.gettid() != 0:
        vssql += "and tenantID = %d " % ve.gettid()
    if ve.gethid() != 0:
        vssql += "and houseID = %d " % ve.gethid()
    if ve.gettname() != "":
        vssql += "and tennatName like '%%%s%%' " % ve.gettname()
    if ve.gethaddress() != "":
        vssql += "and houseAddress like '%%%s%%' " % ve.gethaddress()
    cur.execute(vssql)
    viewings = cur.fetchall()

    return viewings

