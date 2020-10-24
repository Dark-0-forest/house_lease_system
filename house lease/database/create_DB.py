"""
@作者：余宗源
@文件名：create_DB.py
@时间：2020/9/17
@文档说明: 将各个创建函数的包导入，并且调用函数进行创建
"""

import create_datebase as cd
import create_landlord as cl
import create_house as ch
import create_tenant as ct
import create_viewing as cv
import create_admin as ca

cd.create_database()
cl.createlandlord()
ch.createhouse()
ct.createtenant()
cv.createviewing()
ca.createadmin()
