# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pokecontrol.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(595, 275)
        self.btn_up = QtWidgets.QPushButton(Form)
        self.btn_up.setGeometry(QtCore.QRect(70, 70, 41, 41))
        self.btn_up.setObjectName("btn_up")
        self.btn_home = QtWidgets.QPushButton(Form)
        self.btn_home.setGeometry(QtCore.QRect(150, 20, 71, 31))
        self.btn_home.setObjectName("btn_home")
        self.btn_left = QtWidgets.QPushButton(Form)
        self.btn_left.setGeometry(QtCore.QRect(30, 110, 41, 41))
        self.btn_left.setObjectName("btn_left")
        self.btn_right = QtWidgets.QPushButton(Form)
        self.btn_right.setGeometry(QtCore.QRect(110, 110, 41, 41))
        self.btn_right.setObjectName("btn_right")
        self.btn_down = QtWidgets.QPushButton(Form)
        self.btn_down.setGeometry(QtCore.QRect(70, 150, 41, 41))
        self.btn_down.setObjectName("btn_down")
        self.btn_B = QtWidgets.QPushButton(Form)
        self.btn_B.setGeometry(QtCore.QRect(260, 150, 41, 41))
        self.btn_B.setObjectName("btn_B")
        self.btn_A = QtWidgets.QPushButton(Form)
        self.btn_A.setGeometry(QtCore.QRect(300, 110, 41, 41))
        self.btn_A.setObjectName("btn_A")
        self.btn_Y = QtWidgets.QPushButton(Form)
        self.btn_Y.setGeometry(QtCore.QRect(220, 110, 41, 41))
        self.btn_Y.setObjectName("btn_Y")
        self.btn_X = QtWidgets.QPushButton(Form)
        self.btn_X.setGeometry(QtCore.QRect(260, 70, 41, 41))
        self.btn_X.setObjectName("btn_X")
        self.btn_upright = QtWidgets.QPushButton(Form)
        self.btn_upright.setGeometry(QtCore.QRect(110, 70, 41, 41))
        self.btn_upright.setObjectName("btn_upright")
        self.btn_downright = QtWidgets.QPushButton(Form)
        self.btn_downright.setGeometry(QtCore.QRect(110, 150, 41, 41))
        self.btn_downright.setObjectName("btn_downright")
        self.btn_downleft = QtWidgets.QPushButton(Form)
        self.btn_downleft.setGeometry(QtCore.QRect(30, 150, 41, 41))
        self.btn_downleft.setObjectName("btn_downleft")
        self.btn_upleft = QtWidgets.QPushButton(Form)
        self.btn_upleft.setGeometry(QtCore.QRect(30, 70, 41, 41))
        self.btn_upleft.setObjectName("btn_upleft")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 20, 160, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_func1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_func1.setObjectName("btn_func1")
        self.verticalLayout.addWidget(self.btn_func1)
        self.btn_func2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_func2.setObjectName("btn_func2")
        self.verticalLayout.addWidget(self.btn_func2)
        self.btn_func3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_func3.setObjectName("btn_func3")
        self.verticalLayout.addWidget(self.btn_func3)
        self.btn_func4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_func4.setObjectName("btn_func4")
        self.verticalLayout.addWidget(self.btn_func4)
        self.btn_func5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_func5.setObjectName("btn_func5")
        self.verticalLayout.addWidget(self.btn_func5)
        self.btn_ZL = QtWidgets.QPushButton(Form)
        self.btn_ZL.setGeometry(QtCore.QRect(30, 20, 41, 31))
        self.btn_ZL.setObjectName("btn_ZL")
        self.btn_ZR = QtWidgets.QPushButton(Form)
        self.btn_ZR.setGeometry(QtCore.QRect(300, 20, 41, 31))
        self.btn_ZR.setObjectName("btn_ZR")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_up.setText(_translate("Form", "↑"))
        self.btn_home.setText(_translate("Form", "🏠"))
        self.btn_left.setText(_translate("Form", "←"))
        self.btn_right.setText(_translate("Form", "→"))
        self.btn_down.setText(_translate("Form", "↓"))
        self.btn_B.setText(_translate("Form", "B"))
        self.btn_A.setText(_translate("Form", "A"))
        self.btn_Y.setText(_translate("Form", "Y"))
        self.btn_X.setText(_translate("Form", "X"))
        self.btn_upright.setText(_translate("Form", "↗"))
        self.btn_downright.setText(_translate("Form", "↘"))
        self.btn_downleft.setText(_translate("Form", "↙"))
        self.btn_upleft.setText(_translate("Form", "↖"))
        self.btn_func1.setText(_translate("Form", "F1"))
        self.btn_func2.setText(_translate("Form", "F2"))
        self.btn_func3.setText(_translate("Form", "F3"))
        self.btn_func4.setText(_translate("Form", "F4"))
        self.btn_func5.setText(_translate("Form", "F5"))
        self.btn_ZL.setText(_translate("Form", "ZL"))
        self.btn_ZR.setText(_translate("Form", "ZR"))

