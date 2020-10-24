"""
@作者：余宗源
@文件名：landlord_entity.py
@时间：2020/9/18
@文档说明: 完成关于房主的实体类的定义
"""


# 房主的实体类
class Landlord:
    __lid = 0
    __lname = ""
    __laddress = ""
    __lphone = ""
    __luame = ""
    __lpwd = ""

    # landlordID的设置获取函数
    def setlid(self, lid):
        self.__lid = lid

    def getlid(self):
        return self.__lid

    # landlordName的设置获取函数
    def setlname(self, lname):
        self.__lname = lname

    def getlname(self):
        return self.__lname

    # landlordAddress的设置获取函数
    def setladdress(self, laddress):
        self.__laddress = laddress

    def getladdress(self):
        return self.__laddress

    # LphoneNum的设置获取函数
    def setlphone(self, lphone):
        self.__lphone  = lphone

    def getlphone(self):
        return self.__lphone

    # LUserName的设置获取函数
    def setluname(self, luname):
        self.__luame = luname

    def getluname(self):
        return self.__luame

    # LPassword的设置获取函数
    def setlpwd(self, lpwd):
        self.__lpwd = lpwd

    def getlpwd(self):
        return self.__lpwd
