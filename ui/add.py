# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add.ui'
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
        self.label.setGeometry(QtCore.QRect(75, 50, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(75, 100, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(75, 150, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.condition = QtWidgets.QLineEdit(Dialog)
        self.condition.setGeometry(QtCore.QRect(150, 50, 175, 25))
        self.condition.setObjectName("condition")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(150, 100, 175, 25))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(150, 150, 175, 25))
        self.password.setObjectName("password")
        self.ensureBtn = QtWidgets.QPushButton(Dialog)
        self.ensureBtn.setGeometry(QtCore.QRect(75, 205, 100, 35))
        self.ensureBtn.setObjectName("ensureBtn")
        self.cancelBtn = QtWidgets.QPushButton(Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(225, 205, 100, 35))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加"))
        self.label.setText(_translate("Dialog", "情况："))
        self.label_2.setText(_translate("Dialog", "账号："))
        self.label_3.setText(_translate("Dialog", "密码："))
        self.ensureBtn.setText(_translate("Dialog", "确定"))
        self.cancelBtn.setText(_translate("Dialog", "取消"))
