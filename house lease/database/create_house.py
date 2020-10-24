"""
@作者：余宗源
@文件名：create_house.py
@时间：2020/9/17
@文档说明: 存放创建house表的函数，供上层调用
"""

import mysql_connection as mct


# 创建house表，房屋信息表
def createhouse():
    # 初始化mysql的连接
    conn = mct.create_connection()
    cur = conn.cursor()

    # 执行创建表的语句
    clsql = ("create table houselease.house( "
             "houseID       int primary key AUTO_INCREMENT,"
             "houseAddress  varchar(255),"
             "houseNum      int," 
             "landlordID    int not null,"
             "houseType     varchar(255),"
             "furnished     varchar(255),"
             "houseArea     float,"
             "floor         int check(floor >= 1),"
             "lift          varchar(55),"
             "maxtenant     int check(maxtenant >= 1),"
             "rent          float check(rent > 0),"
             "leased        varchar(55) );")
    cur.execute(clsql)
    # 自增变量初始化(其中20表示20年，2表示房屋，000表示自增编号)
    aisql = "alter table houselease.house AUTO_INCREMENT=202000;"
    cur.execute(aisql)

    # 关闭调用
    mct.close_conn(conn, cur)
