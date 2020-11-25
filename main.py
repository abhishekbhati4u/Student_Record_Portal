# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
MySchool=sqlite3.connect('students.db')
sql="SELECT * FROM users"

class Ui_Form(object):
    def click(self):
        QMessageBox.about(self, "Error", "Invalid")
    def chkPassword(self):
        usr=self.username.text()
        pswd=self.password.text()
        curschool=MySchool.cursor()
        curschool.execute(sql)
        result=curschool.fetchall()
        temp=0
        for rec in result:
            if usr==rec[0] and pswd==rec[1]:
                print("Valid Password")
                temp=1
                import submit
                submit.show()
        if temp==0:
            print("Invalid Password")
            self.click()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(662, 569)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        Form.setFont(font)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 180, 261, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.username = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(200, 260, 261, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.horizontalLayout_2.addWidget(self.password)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(270, 340, 191, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.okButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_3.addWidget(self.okButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 450, 681, 78))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 30, 681, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 517, 641, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")

        self.okButton.clicked.connect(self.chkPassword)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.password.clear)
        self.pushButton_2.clicked.connect(self.username.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "Password"))
        self.okButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "RESET"))
        self.label_4.setText(_translate("Form", "Developed By: Abhishek Bhati, Sanchit Goel and Chaitanya Goel"))
        self.label_3.setText(_translate("Form", "WELCOME TO STUDENT RECORD SYSTEM"))
        self.label_5.setText(_translate("Form", "<a href=\"https://github.com/abhishekbhati4u/Student_Record_Portal\">GitHub Project Link</a>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
