# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glav.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 311, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 10, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(330, 50, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Доходы"))
        self.pushButton_3.setText(_translate("Form", "Расходы"))
        self.pushButton.setText(_translate("Form", "Изменения"))
