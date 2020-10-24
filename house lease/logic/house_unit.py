"""
@作者：余宗源
@文件名：house_unit.py
@时间：2020/9/18
@文档说明: 完成关于房屋信息的一些操作，并将其封装为函数，为上层调用提供接口
"""

import mysql_connection as mct


# 插入房屋信息
def house_insert(he):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 插入房屋信息
    sql = "insert into houselease.house values(null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (he.gethaddress(), he.gethnum(), he.getlid(), he.gethtype(), he.getfurnish(), he.getharea(),
                      he.getfloor(), he.getlift(), he.getmaxtenant(), he.getrent(), he.getleased(), he.getcharge()))
    conn.commit()
    # 获取房号
    sql = "select landlordID from houselease.house where  houseAddress = %s and houseNum = %s"
    cur.execute(sql, (he.gethaddress(), he.gethnum()))
    he.sethid(cur.fetchall()[0][0])

    # 关闭调用
    mct.close_conn(conn, cur)


# 修改房屋的信息
def house_update(he):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 更新值
    sql = "update houselease.house set houseAddress = %s, houseNum = %s, houseType = %s, furnished = %s, " \
          "houseArea = %s, floor = %s, lift = %s, maxtenant = %s, rent = %s, leased = %s where houseID = %s"
    cur.execute(sql, (he.gethaddress(), he.gethnum(), he.gethtype(), he.getfurnish(), he.getharea(),
                      he.getfloor(), he.getlift(), he.getmaxtenant(), he.getrent(), he.getleased(), he.gethid()))
    conn.commit()

    # 关闭调用
    mct.close_conn(conn, cur)


# 根据条件对house表进行查询
def house_select(he):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()
    # 根据条件查询
    sql = "select * from houselease.house where 1 "
    if he.gethid() != 0:
        sql += "and houseID = %d " % he.gethid()
    if he.gethaddress() != "":
        sql += "and houseAddress like '%%%s%%' " % he.gethaddress()
    if he.gethnum() != "":
        sql += "and houseNum like '%%%s%%' " % str(he.gethnum())
    if he.getlid() != 0:
        sql += "and landlordID like '%s' " % str(he.getlid())
    if he.gethtype() != "":
        sql += "and houseType like '%%%s%%' " % he.gethtype()
    if he.getfurnish() != "":
        sql += "and furnished like '%s' " % he.getfurnish()
    if he.getharea() != 0:
        sql += "and houseArea >= %f and houseArea <= %f " % (he.getharea()-20, he.getharea()+20)
    if he.getfloor() != "":
        sql += "and floor = '%s' " % he.getfloor()
    if he.getlift() != "":
        sql += "and lift = '%s' " % he.getlift()
    if he.getmaxtenant() != "":
        sql += "and maxtenant = '%s' " % (he.getmaxtenant())
    if he.getrent() != 0:
        sql += "and rent >= %f and rent <= %f " % (he.getrent()-1000.0, he.getrent()+1000.0)
    if he.getleased() != "":
        sql += "and leased = '%s' " % he.getleased()
    cur.execute(sql)
    houses = cur.fetchall()

    # 关闭调用
    mct.close_conn(conn, cur)

    return houses


# 删除记录
def house_delete(he):
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 根据编号删除
    sql = "delete from houselease.house where houseID = %s"
    cur.execute(sql, (he.gethid(), ))
    conn.commit()

    # 关闭调用
    mct.close_conn(conn, cur)







