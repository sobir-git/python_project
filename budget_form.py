# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'budget_form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def OpenWindow(self):
        budget_value= Ui_MainWindow(self)
        budget_value.income_edit.setText(self.income_edit.text())
        budget_value.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(396, 290)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.income_edit = QtGui.QLineEdit(self.centralwidget)
        self.income_edit.setGeometry(QtCore.QRect(160, 70, 113, 20))
        self.income_edit.setObjectName(_fromUtf8("income_edit"))
        
        

        self.savings_edit = QtGui.QLineEdit(self.centralwidget)
        self.savings_edit.setGeometry(QtCore.QRect(160, 100, 113, 20))
        self.savings_edit.setObjectName(_fromUtf8("savings_edit"))


        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))


        self.ok_button = QtGui.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(70, 180, 75, 23))
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.cancel_button = QtGui.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(200, 180, 75, 23))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))

        self.answer_box = QtGui.QLineEdit(self.centralwidget)
        self.answer_box.setGeometry(QtCore.QRect(160, 150, 113, 20))
        self.answer_box.setObjectName(_fromUtf8("answer_box"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 150, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 396, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Income", None))
        self.label_2.setText(_translate("MainWindow", "Savings", None))
        self.label_3.setText(_translate("MainWindow", "Budget App", None))
        self.ok_button.setText(_translate("MainWindow", "OK", None))
        self.cancel_button.setText(_translate("MainWindow", "Cancel", None))
        self.label_4.setText(_translate("MainWindow", "Answer", None))
        self.ok_button.clicked.connect(self.ok_clicked)
        self.cancel_button.clicked.connect(self.cancel_clicked)

    def ok_clicked(self):
        income_value= self.income_edit.text()
        savings_value= self.savings_edit.setText(income_value)
        

    def cancel_clicked(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

