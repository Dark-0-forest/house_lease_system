"""
@作者：余宗源
@文件名：admin_entity.py
@时间：2020/9/18
@文档说明: 完成关于管理员的实体类的定义
"""


# 定义管理员的实体类
class Admin:
    __auname = ""
    __apwd = ""

    # 用户名的获取设置函数
    def setauname(self, auname):
        self.__auname = auname

    def getauname(self):
        return  self.__auname

    # 密码的设置获取函数
    def setapwd(self, apwd):
        self.__apwd = apwd

    def getapwd(self):
        return self.__apwd
