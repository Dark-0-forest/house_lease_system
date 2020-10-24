"""
@作者：余宗源
@文件名：tenant_unit.py
@时间：2020/9/18
@文档说明: 完成关于租户信息的一些操作，并将其封装为函数，为上层调用提供接口
"""

import mysql_connection as mct


# 插入租户信息
def tenant_insert(te):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据用户名和密码插入信息
    sql = "insert into houselease.tenant(TUserName, TPassword) values(%s, %s)"
    cur.execute(sql, (te.gettuname(), te.gettpwd()))
    conn.commit()
    # 获取租户编号
    sql = "select tenantID from houselease.tenant where TUserName = %s and TPassword = %s"
    cur.execute(sql, (te.gettuname(), te.gettpwd()))
    te.settid(cur.fetchall()[0][0])


# 更新租户信息
def tenant_update(te):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 更新租户信息
    sql = "update houselease.tenant set tenantName = %s, tenantAddress = %s, TphoneNum = %s, birthDate = %s," \
          "gender = %s, TUserName = %s where tenantID = %s"
    cur.execute(sql, (te.gettname(), te.gettaddress(), te.gettphone(), te.getbirth(), te.getgender(), te.gettuname(),
                      te.gettid()))
    conn.commit()

    # 关闭调用
    mct.close_conn(conn, cur)


# 删除租户信息
def tenant_delete(te):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据编号删除信息
    tdsql = "delete from houselease.tenant where tenantID = %d " % te.gettid()
    cur.execute(tdsql)
    conn.commit()

    # 关闭调用
    mct.close_conn(conn, cur)


# 查询租户信息
def tenant_select(te):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据条件进行查询
    tssql = "select * from houselease.tenant where 1 "
    if te.gettid() != 0:
        tssql += "and tenantID = %d " % te.gettid()
    if te.gettname() != "":
        tssql += "and tenantName like '%%%s%%' " % te.gettname()
    if te.gettaddress() != "":
        tssql += "and tenantAddress like '%%%s%%' " % te.gettaddress()
    if te.gettphone() != "":
        tssql += "and TphoneNum like '%%%s%%' " % te.gettphone()
    if te.getbirth() != "":
        tssql += "and birthDate like '%%%s%%' " % te.getbirth()
    if te.getgender() != "":
        tssql += "and gender like '%%%s%%' " % te.getgender()
    cur.execute(tssql)
    tenants = cur.fetchall()

    return tenants


# 租客信息的初始化
def tenant_init(te):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据用户名进行查询
    sql = "select * from houselease.tenant where TUserName = %s"
    cur.execute(sql, (te.gettuname(), ))
    data = cur.fetchall()
    te.settid(data[0][0])
    te.settname(data[0][1])
    te.settaddress(data[0][2])
    te.settphone(data[0][3])
    te.setbirth(data[0][4])
    te.setgender(data[0][5])
    te.settuname(data[0][6])


# 租客登录信息查询
def tenant_login(te):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据用户名和密码进行查询
    sql = "select * from houselease.tenant where TUserName = %s and TPassword = %s"
    cur.execute(sql, (te.gettuname(), te.gettpwd()))
    data = cur.fetchone()

    return data


# 用户名查询
def tenant_username(te):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据用户名和密码进行查询
    sql = "select count(*) from houselease.tenant where TUserName = %s"
    cur.execute(sql, (te.gettuname(),))
    data = cur.fetchone()

    return data
