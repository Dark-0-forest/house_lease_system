"""
@作者：余宗源
@文件名：house_entity.py
@时间：2020/9/18
@文档说明: 完成关于房屋的实体类的定义
"""


class House:
    __hid = 0
    __haddress = ""
    __hnum = ""
    __lid = 0
    __htype = ""
    __furnish = ""
    __harea = 0.0
    __floor = ""
    __lift = ""
    __maxtenant = ""
    __charge = 0.0
    __rent = 0.0
    __leased = ""

    # houseID的设置获取函数
    def sethid(self, hid):
        self.__hid = hid

    def gethid(self):
        return self.__hid

    # houseAddress的设置获取函数
    def sethaddress(self, haddress):
        self.__haddress = haddress

    def gethaddress(self):
        return self.__haddress

    # houseNum的设置获取函数
    def sethnum(self, hnum):
        self.__hnum = hnum

    def gethnum(self):
        return self.__hnum

    # landlordID的设置获取函数
    def setlid(self, lid):
        self.__lid = lid

    def getlid(self):
        return self.__lid

    # houseType的设置获取函数
    def sethtype(self, htype):
        self.__htype = htype

    def gethtype(self):
        return self.__htype

    # furnished的设置获取函数
    def setfurnish(self, furnish):
        self.__furnish = furnish

    def getfurnish(self):
        return self.__furnish

    # houseArea的设置获取函数
    def setharea(self, harea):
        self.__harea = harea

    def getharea(self):
        return float(self.__harea)

    # floor的设置获取函数
    def setfloor(self, floor):
        self.__floor = floor

    def getfloor(self):
        return self.__floor

    # lift的设置获取函数
    def setlift(self, lift):
        self.__lift = lift

    def getlift(self):
        return self.__lift

    # maxtenant的设置获取函数
    def setmaxtenant(self, maxtenant):
        self.__maxtenant = maxtenant

    def getmaxtenant(self):
        return self.__maxtenant

    # charge的设置获取函数
    def setcharge(self, charge):
        self.__charge = charge

    def getcharge(self):
        return float(self.__charge)

    # rent的设置获取函数
    def setrent(self, rent):
        self.__rent = rent

    def getrent(self):
        return float(self.__rent)

    # leased的设置获取函数
    def setleased(self, leased):
        self.__leased = leased

    def getleased(self):
        return self.__leased
