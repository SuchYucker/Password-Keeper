# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(75, 75, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(75, 135, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(150, 75, 175, 25))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(150, 135, 175, 25))
        self.password.setObjectName("password")
        self.logBtn = QtWidgets.QPushButton(Dialog)
        self.logBtn.setGeometry(QtCore.QRect(75, 200, 100, 35))
        self.logBtn.setObjectName("logBtn")
        self.quitBtn = QtWidgets.QPushButton(Dialog)
        self.quitBtn.setGeometry(QtCore.QRect(225, 200, 100, 35))
        self.quitBtn.setObjectName("quitBtn")

        self.retranslateUi(Dialog)
        self.username.editingFinished.connect(self.password.selectAll)
        self.quitBtn.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))
        self.label.setText(_translate("Dialog", "账号："))
        self.label_2.setText(_translate("Dialog", "密码："))
        self.logBtn.setText(_translate("Dialog", "登录"))
        self.quitBtn.setText(_translate("Dialog", "退出"))
