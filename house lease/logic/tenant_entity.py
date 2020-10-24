"""
@作者：余宗源
@文件名：tenant_entity.py
@时间：2020/9/18
@文档说明: 完成关于租户的实体类的定义
"""


class Tenant:
    __tid = 0
    __tname = ""
    __taddress = ""
    __tphone = ""
    __birth = ""
    __gender = ""
    __tuname = ""
    __tpwd = ""

    # tenantID的设置获取函数
    def settid(self, tid):
        self.__tid = tid

    def gettid(self):
        return self.__tid

    # tenantName的设置获取函数
    def settname(self, tname):
        self.__tname = tname

    def gettname(self):
        return self.__tname

    # tenantAddress的设置获取函数
    def settaddress(self, taddress):
        self.__taddress = taddress

    def gettaddress(self):
        return self.__taddress

    # TphoneNum的设置获取函数
    def settphone(self, tphone):
        self.__tphone = tphone

    def gettphone(self):
        return self.__tphone

    # birthDate的设置获取函数
    def setbirth(self, birth):
        self.__birth = birth

    def getbirth(self):
        return self.__birth

    # gender的设置获取函数
    def setgender(self, gender):
        self.__gender = gender

    def getgender(self):
        return self.__gender

    # TUseName的设置获取函数
    def settuname(self, tuname):
        self.__tuname = tuname

    def gettuname(self):
        return self.__tuname

    # TPassword的设置获取函数
    def settpwd(self, tpwd):
        self.__tpwd = tpwd

    def gettpwd(self):
        return self.__tpwd
