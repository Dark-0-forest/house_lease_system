import re
import hashlib
import datetime
import resource_rc
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QIcon
from QCandyUi.CandyWindow import colorful
from QCandyUi import CandyWindow
# 实体包
import landlord_entity
import tenant_entity
import admin_entity
import house_entity
import viewing_entity
# 处理单元包
import landlord_unit as lu
import tenant_unit as tu
import admin_unit as au
import house_unit as hu
import viewing_unit as vu

# 获取ui界面
login, _ = loadUiType("ui/login.ui")
register, _ = loadUiType("ui/register.ui")
input_landlord, _ = loadUiType("ui/register_landlord.ui")
input_tenant, _ = loadUiType("ui/register_tenant.ui")
landlord, _ = loadUiType("ui/landlord.ui")
tenant, _ = loadUiType("ui/tenant.ui")
charge, _ = loadUiType("ui/charge.ui")
admin, _ = loadUiType("ui/admin.ui")


# 创建各个实体
le = landlord_entity.Landlord()
te = tenant_entity.Tenant()
ae = admin_entity.Admin()
he = house_entity.House()
ve = viewing_entity.Viewing()


# 用户密码的MD5加密处理
def md5(pwd):
    hash = hashlib.md5(bytes("Darkforest", encoding="utf-8"))
    hash.update(bytes(pwd, encoding="utf-8"))
    return hash.hexdigest()


# 用于匹配电话号码的正则表达式
regex = re.compile(r'1\d{10}')


# 登录界面gui建立
@colorful('blueGreen', '房屋租赁系统登录界面', 'ui/images/mainpage.png')
class LoginApp(QDialog, login):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.login_login_button.clicked.connect(self.handle_login)
        self.login_login_button.setShortcut('return')
        self.login_register_button.clicked.connect(self.handle_register)

    def handle_login(self):
        # 验证登录信息是否正确
        user_name = self.login_user_name.text()
        pwd_md5 = md5(self.login_user_pwd.text())
        current_type = self.login_user_type.currentText()
        if current_type == "房主":
            le.setluname(user_name)
            le.setlpwd(pwd_md5)
            data = lu.landlord_login(le)
            if data:
                self.landlordapp = LandlordApp()
                self.landlordapp.show()
                self.close()
        elif current_type == "租客":
            te.settuname(user_name)
            te.settpwd(pwd_md5)
            data = tu.tenant_login(te)
            if data:
                self.tenantapp = TenantApp()
                self.tenantapp.show()
                self.close()
        elif current_type == "管理员":
            ae.setauname(user_name)
            ae.setapwd(pwd_md5)
            data = au.admin_login(ae)
            if data:
                self.adminapp = AdminApp()
                self.adminapp.show()
                self.close()

        if data:
            pass
        else:
            warning = QMessageBox.warning(self, "错误!", "用户或密码错误", QMessageBox.Yes)
            if warning == QMessageBox.Yes:
                self.login_user_name.setText("")
                self.login_user_pwd.setText("")

    def handle_register(self):
        self.registerapp = RegisterApp()
        self.registerapp.show()


# 注册界面gui建立
class RegisterApp(QDialog, register):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/images/register.png'))
        self.register_register_button.clicked.connect(self.handle_register)
        self.register_register_button.setShortcut('return')

    def handle_register(self):
        # 根据类型将信息插入对应表
        user_name = self.register_username.text()
        type = self.register_type.currentText()
        pwd = self.register_pwd.text()
        confirm_pwd = self.register_confirm_pwd.text()
        if user_name == "":
            self.error_message.setText("用户名不能为空")
        else:
            if pwd == "" and confirm_pwd == "":
                self.error_message.setText("密码不能为空")

            elif pwd == confirm_pwd:
                pwd_md5 = md5(pwd)
                if type == "房主":
                    le.setluname(user_name)
                    le.setlpwd(pwd_md5)
                    user_name_count = lu.landlord_username(le)
                    if user_name_count[0] == 0:
                        lu.landlord_insert(le)
                        self.inputlandlordapp = InputLandlordApp()
                        self.inputlandlordapp.show()
                        self.close()

                    else:
                        self.register_pwd.setText("")
                        self.register_confirm_pwd.setText("")
                        self.register_username.setText("")
                        self.error_message.setText("此用户名已注册")

                elif type == "租客":
                    te.settuname(user_name)
                    te.settpwd(pwd_md5)
                    user_name_count = tu.tenant_username(te)
                    if user_name_count[0] == 0:
                        tu.tenant_insert(te)
                        self.inputtenantapp = InputTenantApp()
                        self.inputtenantapp.show()
                        self.close()

                    else:
                        self.register_pwd.setText("")
                        self.register_confirm_pwd.setText("")
                        self.register_username.setText("")
                        self.error_message.setText("此用户名已注册")

            elif pwd != confirm_pwd:
                self.register_pwd.setText("")
                self.register_confirm_pwd.setText("")
                self.error_message.setText("两次密码不相同")


# 房主信息输入界面gui建立
class InputLandlordApp(QDialog, input_landlord):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show_landlord()
        self.setWindowIcon(QIcon('ui/images/personinfo.png'))
        self.register_information_confirm_button.clicked.connect(self.handle_update)
        self.register_information_confirm_button.setShortcut('return')

    # 显示编号和用户名
    def show_landlord(self):
        self.register_landlord_id.setText(str(le.getlid()))
        self.register_landlord_username.setText(str(le.getluname()))

    # 处理信息的更新
    def handle_update(self):
        name = self.register_landlord_name.text()
        address = self.register_landlord_address.text()
        phone = self.register_landlord_phone.text()
        if name == "" or address == "" or phone == "":
            self.message.setText("请输入所有信息")
        else:
            if re.match(regex, phone):
                le.setlname(name)
                le.setladdress(address)
                le.setlphone(phone)
                lu.landlord_update(le)
                self.close()
            else:
                self.register_landlord_phone.setText("")
                self.message.setText("电话号码应为以1开头的11位数字")


# 租客信息输入界面gui建立
class InputTenantApp(QDialog, input_tenant):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show_tenant()
        self.setWindowIcon(QIcon('ui/images/personinfo.png'))
        self.register_tenant_confirm_button.clicked.connect(self.handle_update)
        self.register_tenant_confirm_button.setShortcut('return')

    # 显示编号和用户名
    def show_tenant(self):
        self.register_tenant_id.setText(str(te.gettid()))
        self.register_tenant_username.setText(te.gettuname())

    # 处理信息的更新
    def handle_update(self):
        name = self.register_tenant_name.text()
        address = self.register_tenant_address.text()
        phone = self.register_tenant_phone.text()
        birth = self.register_tenant_birth.date().toString(Qt.ISODate)
        gender = self.register_tenant_gender.currentText()
        if name == "" or address == "" or phone == "" or birth == "" or gender == "":
            self.message.setText("请输入所有信息")
        else:
            if re.match(regex, phone):
                te.settname(name)
                te.settaddress(address)
                te.settphone(phone)
                te.setbirth(birth)
                te.setgender(gender)
                tu.tenant_update(te)
                self.close()
            else:
                self.register_tenant_phone.setText("")
                self.message.setText("电话号码应为以1开头的11位数字")


# 房主操作界面的建立
@colorful('blue', '房主操作系统', 'ui/images/mainpage.png')
class LandlordApp(QMainWindow, landlord):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui_setting()
        self.handle_button()
        self.show_landlord()
        self.show_house()

    # UI的一些设置
    def ui_setting(self):
        # 标题
        self.setWindowTitle("fangzhu")
        # 将选择框设为不可见
        self.landlord_tabWidget.tabBar().setVisible(False)
        # 每次进入将页面设置位个人信息页面
        self.landlord_tabWidget.setCurrentIndex(0)
        self.person_tabWidget.setCurrentIndex(0)
        #
        self.table = QTableWidget(3, 5)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置几个文本框的默认内容
        self.search_house_type.setPlaceholderText("例：三室两厅一厨一卫")
        self.add_house_type.setPlaceholderText("例：三室两厅一厨一卫")
        self.change_house_type.setPlaceholderText("例：三室两厅一厨一卫")
        # 设置房屋tablewidget的列宽
        self.show_house_table.setColumnWidth(0, 70)
        self.show_house_table.setColumnWidth(1, 140)
        self.show_house_table.setColumnWidth(2, 60)
        self.show_house_table.setColumnWidth(3, 75)
        self.show_house_table.setColumnWidth(4, 150)
        self.show_house_table.setColumnWidth(5, 130)
        self.show_house_table.setColumnWidth(6, 60)
        self.show_house_table.setColumnWidth(7, 45)
        self.show_house_table.setColumnWidth(8, 70)
        self.show_house_table.setColumnWidth(9, 40)
        self.show_house_table.setColumnWidth(10, 70)
        self.show_house_table.setColumnWidth(11, 65)
        self.show_house_table.setColumnWidth(12, 50)

    # 用来处理所有的button的消息和槽直接的通信
    def handle_button(self):
        # 把图标按钮和tabwidget的个人信息关联起来
        self.person_info_button.clicked.connect(self.open_person_info)
        # 把图标按钮和tabwidget的房屋信息关联起来
        self.house_info_button.clicked.connect(self.open_house_info)
        # 个人信息界面的修改button
        self.change_landlord_button.clicked.connect(self.landlord_change)
        self.change_landlord_button.clicked.connect(self.show_landlord)
        # 搜索界面的搜索button
        self.search_house_button.clicked.connect(self.house_search)
        # 添加界面的添加房屋button
        self.add_house_button.clicked.connect(self.house_insert)
        self.add_house_button.clicked.connect(self.show_house)
        # 修改界面中的查询button
        self.change_search_button.clicked.connect(self.house_change_get)
        # 修改界面中的修改button
        self.change_house_button.clicked.connect(self.house_change)
        self.change_house_button.clicked.connect(self.show_house)
        # 修改界面中的删除button
        self.change_house_delete_button.clicked.connect(self.house_delete)
        self.change_house_delete_button.clicked.connect(self.show_house)

    # 获取landlord的基本信息，并展示
    def show_landlord(self):
        lu.landlord_init(le)
        # 查看信息的初始化
        self.show_landlord_id.setText(str(le.getlid()))
        self.show_landlord_username.setText(le.getluname())
        self.show_landlord_name.setText(le.getlname())
        self.show_landlord_address.setText(le.getladdress())
        self.show_landlord_phone.setText(le.getlphone())
        # 修改信息的初始化
        self.change_landlord_username.setText(le.getluname())
        self.change_landlord_name.setText(le.getlname())
        self.change_landlord_address.setText(le.getladdress())
        self.change_landlord_phone.setText(le.getlphone())

    # landlord信息的修改
    def landlord_change(self):
        uname = self.change_landlord_username.text()
        name = self.change_landlord_name.text()
        address = self.change_landlord_address.text()
        phone = self.change_landlord_phone.text()
        if uname == "" or name == "" or address == "" or phone == "":
            self.statusBar().showMessage("请输入全部信息", 5000)
        else:
            le.setluname(uname)
            user_name_count = lu.landlord_username(le)
            print(user_name_count)
            if user_name_count[0] == 0 or uname == le.getluname():
                if re.match(regex, phone):
                    le.setluname(uname)
                    le.setlname(name)
                    le.setladdress(address)
                    le.setlphone(phone)
                    lu.landlord_change(le)
                    self.statusBar().showMessage("房主信息修改成功", 5000)
                else:
                    self.change_landlord_phone.setText("")
                    self.statusBar().showMessage("电话号码应为以1开头的11位数字", 5000)
            else:
                self.change_landlord_username.setText("")
                self.statusBar().showMessage("此用户名已注册", 5000)

    # house信息的show
    def show_house(self):
        # he1是来表示登录房主的所有房屋的实体
        he1 = house_entity.House()
        he1.setlid(le.getlid())
        data = hu.house_select(he1)

        if data:
            self.show_house_table.setRowCount(0)
            self.show_house_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.show_house_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.show_house_table.rowCount()
                self.show_house_table.insertRow(row_position)

    # house信息的search
    def house_search(self):
        # he5是来表示房屋搜索的实体
        he5 = house_entity.House()
        he5.setlid(le.getlid())
        he5.sethaddress(self.search_house_address.text())
        he5.sethnum(self.search_house_num.text())
        he5.setfurnish(self.search_house_furniture.currentText())
        he5.sethtype(self.search_house_type.text())
        he5.setfloor(self.search_house_floor.currentText())
        he5.setlift(self.search_house_lift.currentText())
        he5.setmaxtenant(self.search_house_max.currentText())
        he5.setleased(self.search_house_leased.currentText())
        data = hu.house_select(he5)

        self.show_house_table.setRowCount(0)
        self.show_house_table.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.show_house_table.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.show_house_table.rowCount()
            self.show_house_table.insertRow(row_position)

    # house信息的插入
    def house_insert(self):
        if (self.add_house_address.text() == "" or self.add_house_num.text() == "" or self.add_house_type.text() == ""
                or self.add_house_area.text() == "" or self.add_house_rent.text() == ""):
            self.statusBar().showMessage("请输入所有信息", 5000)
        else:
            he.sethaddress(self.add_house_address.text())
            he.sethnum(self.add_house_num.text())
            he.setlid(le.getlid())
            he.sethtype(self.add_house_type.text())
            he.setfurnish(self.add_house_furniture.currentText())
            he.setharea(self.add_house_area.text())
            he.setfloor(self.add_house_floor.currentText())
            he.setlift(self.add_house_lift.currentText())
            he.setmaxtenant(self.add_house_max.currentText())
            he.setcharge(float(self.add_house_area.text()) + float(self.add_house_floor.currentText()) * 3.0)
            he.setrent(self.add_house_rent.text())
            he.setleased(self.add_house_leased.currentText())
            hu.house_insert(he)
            self.chargeapp = HousechargeApp()
            self.chargeapp.show()
            self.statusBar().showMessage("房屋信息添加成功", 8000)
            self.add_house_address.setText("")
            self.add_house_num.setText("")
            self.add_house_type.setText("")
            self.add_house_area.setText("")
            self.add_house_rent.setText("")
            self.add_house_leased.setCurrentIndex(0)

    # 通过房号来获取信息并将其写在修改页面的各栏中
    def house_change_get(self):
        # he2是用来查找特定房号的房屋实体
        he2 = house_entity.House()
        he2.sethid(int(self.change_house_id.text()))
        data = hu.house_select(he2)

        if data:
            self.statusBar().showMessage("房屋信息查找成功", 5000)
            self.change_house_address.setText(data[0][1])
            self.change_house_num.setText(data[0][2])
            self.change_house_type.setText(data[0][4])
            self.change_house_furniture.setCurrentText(data[0][5])
            self.change_house_area.setText(str(data[0][6]))
            self.change_house_floor.setCurrentText(str(data[0][7]))
            self.change_house_lift.setCurrentText(data[0][8])
            self.change_house_max.setCurrentText(str(data[0][9]))
            self.change_house_rent.setText(str(data[0][10]))
            self.change_house_leased.setCurrentText(data[0][11])
        else:
            self.statusBar().showMessage("未查找到对应的房屋信息，请检查房屋编号是否正确", 5000)

    # 修改房屋的信息
    def house_change(self):
        if (self.change_house_address.text()=="" or self.change_house_num.text()=="" or self.change_house_type.text() ==
        "" or self.change_house_area.text() == "" or self.change_house_rent.text() == ""):
            self.statusBar().showMessage("请输入所有信息", 5000)
        else:
            # he3是用来修改特定房号的房屋实体
            he3 = house_entity.House()
            he3.sethid(self.change_house_id.text())
            he3.sethaddress(self.change_house_address.text())
            he3.sethnum(self.change_house_num.text())
            he3.sethtype(self.change_house_type.text())
            he3.setfurnish(self.change_house_furniture.currentText())
            he3.setharea(self.change_house_area.text())
            he3.setfloor(self.change_house_floor.currentText())
            he3.setlift(self.change_house_lift.currentText())
            he3.setmaxtenant(self.change_house_max.currentText())
            he3.setrent(self.change_house_rent.text())
            he3.setleased(self.change_house_leased.currentText())
            hu.house_update(he3)
            self.statusBar().showMessage("房屋信息修改成功", 5000)

    # 删除房屋信息
    def house_delete(self):
        # he4是用来删除特定房号的房屋实体
        he4 = house_entity.House()
        he4.sethid(self.change_house_id.text())
        hu.house_delete(he4)
        self.change_house_address.setText("")
        self.change_house_num.setText("")
        self.change_house_type.setText("")
        self.change_house_furniture.setCurrentIndex(0)
        self.change_house_area.setText("")
        self.change_house_floor.setCurrentIndex(0)
        self.change_house_lift.setCurrentIndex(0)
        self.change_house_max.setCurrentIndex(0)
        self.change_house_rent.setText("")
        self.change_house_leased.setCurrentIndex(0)
        self.statusBar().showMessage("房屋信息删除成功", 5000)

    # 选项卡的绑定
    def open_person_info(self):
        self.landlord_tabWidget.setCurrentIndex(0)
        self.person_tabWidget.setCurrentIndex(0)

    def open_house_info(self):
        self.landlord_tabWidget.setCurrentIndex(1)
        self.house_tabWidget.setCurrentIndex(0)


# 租客操作界面的建立
@colorful('blue', '租客操作系统', 'ui/images/mainpage.png')
class TenantApp(QMainWindow, tenant):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui_setting()
        self.button()
        self.show_tenant()
        self.house_search()

    # UI的一些设置
    def ui_setting(self):
        # 将选择框设为不可见
        self.tenant_tabWidget.tabBar().setVisible(False)
        # 每次进入将页面设置位个人信息页面
        self.tenant_tabWidget.setCurrentIndex(0)
        self.person_tabWidget.setCurrentIndex(0)
        # 设置房屋tablewidget的列宽
        self.show_house_table.setColumnWidth(0, 70)
        self.show_house_table.setColumnWidth(1, 150)
        self.show_house_table.setColumnWidth(2, 55)
        self.show_house_table.setColumnWidth(3, 70)
        self.show_house_table.setColumnWidth(4, 180)
        self.show_house_table.setColumnWidth(5, 120)
        self.show_house_table.setColumnWidth(6, 60)
        self.show_house_table.setColumnWidth(7, 45)
        self.show_house_table.setColumnWidth(8, 60)
        self.show_house_table.setColumnWidth(9, 40)
        self.show_house_table.setColumnWidth(10, 70)
        self.show_house_table.setColumnWidth(11, 70)

    # 所有button的处理
    def button(self):
        # 将图标和界面绑定
        self.person_info_button.clicked.connect(self.open_person_info)
        self.house_info_button.clicked.connect(self.open_house_info)
        # 个人信息界面中的修改信息button
        self.change_tenant_button.clicked.connect(self.tenant_change)
        self.change_tenant_button.clicked.connect(self.show_tenant)
        # 房屋信息中的搜索button
        self.search_house_button.clicked.connect(self.house_search)
        # 看房中的搜索button
        self.house_viewing_search_button.clicked.connect(self.house_num_search)
        # 看房中的看房button
        self.house_viewing_confirm_button.clicked.connect(self.viewing)

    # 显示租客的个人信息
    def show_tenant(self):
        # 先对租客进行初始化
        tu.tenant_init(te)
        # 对show界面的内容填写
        self.show_tenant_id.setText(str(te.gettid()))
        self.show_tenant_name.setText(te.gettname())
        self.show_tenant_address.setText(te.gettaddress())
        self.show_tenant_phone.setText(te.gettphone())
        self.show_tenant_username.setText(te.gettuname())
        self.show_tenant_birthdate.setText(te.getbirth().strftime("%Y/%m/%d"))
        self.show_tenant_gender.setText(te.getgender())
        # 对change界面的内容填写
        self.change_tenant_username.setText(te.gettuname())
        self.change_tenant_name.setText(te.gettname())
        self.change_tenant_address.setText(te.gettaddress())
        self.change_tenant_phone.setText(te.gettphone())
        self.change_tenant_birthdate.setDate(te.getbirth())
        self.change_tenant_gender.setCurrentText(te.getgender())

    # 修改租客的个人信息
    def tenant_change(self):
        uname = self.change_tenant_username.text()
        name = self.change_tenant_name.text()
        address = self.change_tenant_address.text()
        phone = self.change_tenant_phone.text()
        birthdate = self.change_tenant_birthdate.date().toPyDate()
        gender = self.change_tenant_gender.currentText()
        if uname == "" or name == "" or address == "" or phone == "":
            self.statusBar().showMessage("请输入全部信息", 5000)
        else:
            user_name_count = tu.tenant_username(te)
            if user_name_count[0] == 0 or uname == te.gettuname():
                if re.match(regex, phone):
                    te.settuname(uname)
                    te.settname(name)
                    te.settaddress(address)
                    te.settphone(phone)
                    te.setbirth(birthdate)
                    te.setgender(gender)
                    tu.tenant_update(te)
                    self.statusBar().showMessage("房主信息修改成功", 5000)
                else:
                    self.change_tenant_phone.setText("")
                    self.statusBar().showMessage("电话号码应为以1开头的11位数字", 5000)
            else:
                self.change_tenant_username.setText("")
                self.statusBar().showMessage("此用户名已注册", 5000)

    # 房屋的查询
    def house_search(self):
        he1 = house_entity.House()
        he1.sethaddress(self.search_house_address.text())
        he1.sethtype(self.search_house_type.text())
        he1.setmaxtenant(self.search_house_max.currentText())
        he1.setfurnish(self.search_house_furniture.currentText())
        he1.setlift(self.search_house_lift.currentText())
        he1.setfloor(self.search_house_floor.currentText())
        he1.setleased("未出租")
        data = hu.house_select(he1)

        if data:
            self.show_house_table.setRowCount(0)
            self.show_house_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.show_house_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.show_house_table.rowCount()
                self.show_house_table.insertRow(row_position)

    # 房号查询
    def house_num_search(self):
        # he2是用来查找特定房号的房屋实体
        he2 = house_entity.House()
        he2.sethid(int(self.house_viewing_id.text()))
        data = hu.house_select(he2)

        if data:
            self.statusBar().showMessage("房屋信息查找成功", 5000)
            self.house_viewing_address.setText(data[0][1])
            self.house_viewing_num.setText(data[0][2])
            ve.sethid(data[0][0])
            ve.settid(data[0][3])
            ve.settname(te.gettname())
            ve.sethaddress(data[0][1])

        else:
            self.house_viewing_id.setText("")
            self.statusBar().showMessage("请检查您输入的房屋编号是否正确", 5000)
            self.house_viewing_address.setText("")
            self.house_viewing_num.setText("")

    # 看房手续费收费单生成
    def viewing(self):
        self.viewapp = ViewchargeApp()
        self.viewapp.show()

    # 选项卡的绑定
    def open_person_info(self):
        self.tenant_tabWidget.setCurrentIndex(0)
        self.person_tabWidget.setCurrentIndex(0)

    def open_house_info(self):
        self.tenant_tabWidget.setCurrentIndex(1)
        self.house_viewing.setCurrentIndex(0)


# 房屋手续费收费单gui建立
class HousechargeApp(QDialog, charge):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.handle()
        self.setWindowIcon(QIcon('ui/images/charge.png'))
        self.charge_confirm.clicked.connect(self.close)

    def handle(self):
        self.charge_title.setText("房屋手续费收费单")
        self.charge_houseid.setText(str(he.gethid()))
        self.charge_type.setText("房主编号:")
        self.charge_landlordname.setText(str(he.getlid()))
        self.charge_amount.setText(str(he.getcharge()))
        self.charge_time.setText(str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))


# 看房手续费收费单gui建立
class ViewchargeApp(QDialog, charge):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.handle()
        self.setWindowIcon(QIcon('ui/images/charge.png'))
        self.charge_confirm.clicked.connect(self.close)

    def handle(self):
        self.charge_title.setText("看房手续费收费单")
        self.charge_houseid.setText(str(ve.gethid()))
        self.charge_type.setText("租客编号:")
        self.charge_landlordname.setText(str(ve.gettid()))
        self.charge_amount.setText(str(ve.getcharge()))
        self.charge_time.setText(ve.getvdate())
        vu.viewing_insert(ve)


# 管理员操作界面的建立
@colorful('blue', '管理员操作系统', 'ui/images/mainpage.png')
class AdminApp(QMainWindow, admin):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui_setting()
        self.button()
        self.show_landlord()
        self.show_tenant()
        self.show_house()
        self.show_viewing()

    # UI的一些设置
    def ui_setting(self):
        # 将选择框设为不可见
        self.tenant_tab.tabBar().setVisible(False)

    # 所有button的处理
    def button(self):
        # 将图标和对应选项卡关联起来
        self.landlord_button.clicked.connect(self.open_landlord)
        self.tenant_button.clicked.connect(self.open_tenant)
        self.house_button.clicked.connect(self.open_house)
        self.viewing_button.clicked.connect(self.open_viewing)

    def show_landlord(self):
        # 列宽设置
        self.landlord_tab.setColumnWidth(2, 250)
        # 获取并显示数据
        le_admin = landlord_entity.Landlord()
        data = lu.landlord_select(le_admin)
        if data:
            self.landlord_tab.setRowCount(0)
            self.landlord_tab.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.landlord_tab.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.landlord_tab.rowCount()
                self.landlord_tab.insertRow(row_position)

    def show_tenant(self):
        # 列宽设置
        self.tenant_tab_2.setColumnWidth(2, 250)
        # 获取并显示数据
        te_admin = tenant_entity.Tenant()
        data = tu.tenant_select(te_admin)
        if data:
            self.tenant_tab_2.setRowCount(0)
            self.tenant_tab_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tenant_tab_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tenant_tab_2.rowCount()
                self.tenant_tab_2.insertRow(row_position)

    def show_house(self):
        # 列宽设置
        self.house_tab.setColumnWidth(0, 65)
        self.house_tab.setColumnWidth(1, 200)
        self.house_tab.setColumnWidth(2, 55)
        self.house_tab.setColumnWidth(3, 70)
        self.house_tab.setColumnWidth(4, 150)
        self.house_tab.setColumnWidth(5, 110)
        self.house_tab.setColumnWidth(6, 60)
        self.house_tab.setColumnWidth(7, 40)
        self.house_tab.setColumnWidth(8, 60)
        self.house_tab.setColumnWidth(9, 40)
        self.house_tab.setColumnWidth(10, 60)
        self.house_tab.setColumnWidth(11, 60)
        self.house_tab.setColumnWidth(12, 50)

        # 获取并显示数据
        he_admin = house_entity.House()
        data = hu.house_select(he_admin)
        if data:
            self.house_tab.setRowCount(0)
            self.house_tab.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.house_tab.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.house_tab.rowCount()
                self.house_tab.insertRow(row_position)

    def show_viewing(self):
        # 列宽设置
        self.viewing_tab.setColumnWidth(4, 250)
        # 获取并显示数据
        ve_admin = viewing_entity.Viewing()
        data = vu.viewing_select(ve_admin)
        if data:
            self.viewing_tab.setRowCount(0)
            self.viewing_tab.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.viewing_tab.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.viewing_tab.rowCount()
                self.viewing_tab.insertRow(row_position)

    def open_landlord(self):
        self.tenant_tab.setCurrentIndex(0)

    def open_tenant(self):
        self.tenant_tab.setCurrentIndex(1)

    def open_house(self):
        self.tenant_tab.setCurrentIndex(2)

    def open_viewing(self):
        self.tenant_tab.setCurrentIndex(3)


# 界面的show函数
def main():
    app = QApplication([])
    window = LoginApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
