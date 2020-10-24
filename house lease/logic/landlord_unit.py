"""
@作者：余宗源
@文件名：landlord_unit.py
@时间：2020/9/18
@文档说明: 完成关于房主信息的一些操作，并将其封装为函数，为上层调用提供接口
"""

import mysql_connection as mct


# 插入房主信息
def landlord_insert(le):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 插入房主信息
    sql = "insert into houselease.landlord(LUserName, LPassword) values (%s, %s)"
    cur.execute(sql, (le.getluname(), le.getlpwd()))
    conn.commit()

    # 获取房主ID
    sql = "select landlordID from houselease.landlord where  LUserName= %s and LPassword = %s"
    cur.execute(sql, (le.getluname(), le.getlpwd()))
    le.setlid(cur.fetchall()[0][0])


# 更新房主信息
def landlord_update(le):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 更新房主信息
    sql = "update houselease.landlord set  landlordName= %s, landlordAddress = %s, LphoneNum = %s where landlordID = %s"
    cur.execute(sql, (le.getlname(), le.getladdress(), le.getlphone(), le.getlid()))
    conn.commit()

    # 关闭调用
    mct.close_conn(conn, cur)


# 修改房主信息
def landlord_change(le):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 更新房主信息
    sql = "update houselease.landlord set landlordName= %s, landlordAddress = %s, LphoneNum = %s, LUserName = %s " \
          "where landlordID = %s"
    cur.execute(sql, (le.getlname(), le.getladdress(), le.getlphone(), le.getluname(), le.getlid()))
    conn.commit()

    # 关闭调用
    mct.close_conn(conn, cur)

# 根据条件查询房主信息
def landlord_select(le):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据条件查询
    sql = "select * from houselease.landlord where 1 "
    if le.getlname() != '':
        sql += "and landlordName like '%%%s%%' " % le.getlname()
    if le.getladdress() != '':
        sql += "and landlordAddress like '%%%s%%' " % le.getladdress()
    if le.getlphone() != '':
        sql += "and LphoneNum like '%%%s%%' " % le.getlphone()
    cur.execute(sql)
    landlords = cur.fetchall()

    return landlords


# 根据用户名初始化landlord的实体
def landlord_init(le):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    sql = "select * from houselease.landlord where LUserName = %s"
    cur.execute(sql, (le.getluname(), ))
    data = cur.fetchall()
    le.setlid(data[0][0])
    le.setlname(data[0][1])
    le.setladdress(data[0][2])
    le.setlphone(data[0][3])
    le.setluname(data[0][4])


# 查找登录信息
def landlord_login(le):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据用户名和密码进行查询
    sql = "select * from houselease.landlord where LUserName = %s and LPassword = %s"
    cur.execute(sql, (le.getluname(), le.getlpwd()))
    data = cur.fetchone()

    return data


# 查找用户名是否已使用
def landlord_username(le):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据用户名和密码进行查询
    sql = "select count(*) from houselease.landlord where LUserName = %s"
    cur.execute(sql, (le.getluname(), ))
    data = cur.fetchone()

    return data
