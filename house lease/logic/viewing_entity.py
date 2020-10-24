"""
@作者：余宗源
@文件名：viewing_entity.py
@时间：2020/9/18
@文档说明: 完成关于看房记录的实体类的定义
"""

import datetime
import random
# 获取今天的日期

class Viewing:
    __tid = 0
    __hid = 0
    __tname = ""
    __haddress = ""

    # tenantID的设置获取函数
    def settid(self, tid):
        self.__tid = tid

    def gettid(self):
        return self.__tid

    # houseID的设置获取函数
    def sethid(self, hid):
        self.__hid = hid

    def gethid(self):
        return self.__hid

    # tenantName的设置获取函数
    def settname(self, tname):
        self.__tname = tname

    def gettname(self):
        return self.__tname

    # address的设置获取函数
    def sethaddress(self, address):
        self.__haddress = address

    def gethaddress(self):
        return self.__haddress

    # charge的设置获取函数
    def getcharge(self):
        return random.randint(80, 110)

    # viewDate的获取函数
    def getvdate(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
