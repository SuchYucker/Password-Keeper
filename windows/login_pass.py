# -*- coding: utf-8 -*-

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QDialog, QMessageBox

from Sql.Sql import MySql
from ui.login import Ui_Dialog as loginPassUI
from windows.mainwindow_pass import MainWindow


class LoginPass(loginPassUI, QDialog):
    def __init__(self):
        super(LoginPass, self).__init__()
        self.setupUi(self)
        self.main_windows = MainWindow()
        self.logBtn.clicked.connect(self.login_system)
        self.quitBtn.clicked.connect(QCoreApplication.instance().quit)
        self.users=MySql.login()

    def login_system(self):
        jug = 0
        for n in range(len(self.users)):
            username = self.users[n][0]
            password = self.users[n][1]
            if bool(self.username.text() == username) & bool(self.password.text() == password):
                jug = 1
                break
        if jug == 1:
            self.main_windows.show()
            self.close()
        else:
            QMessageBox.about(self, "系统提示", "您输入的账号或密码有误,请检查后登陆.")
