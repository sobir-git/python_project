# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goal_clock.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(210, 331)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout.setLayout(2, QtGui.QFormLayout.LabelRole, self.verticalLayout)
        self.pay_rate = QtGui.QLineEdit(self.centralwidget)
        self.pay_rate.setObjectName(_fromUtf8("pay_rate"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pay_rate)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout.setLayout(4, QtGui.QFormLayout.LabelRole, self.verticalLayout_2)
        self.target_purchase = QtGui.QLineEdit(self.centralwidget)
        self.target_purchase.setObjectName(_fromUtf8("target_purchase"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.target_purchase)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout.setLayout(5, QtGui.QFormLayout.LabelRole, self.verticalLayout_3)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.label_3)
        self.per_month_pay = QtGui.QSpinBox(self.centralwidget)
        self.per_month_pay.setObjectName(_fromUtf8("per_month_pay"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.per_month_pay)
        self.day_until_purchase = QtGui.QLineEdit(self.centralwidget)
        self.day_until_purchase.setObjectName(_fromUtf8("day_until_purchase"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.day_until_purchase)
        self.ok_button = QtGui.QPushButton(self.centralwidget)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.FieldRole, self.ok_button)
        self.reset_button = QtGui.QPushButton(self.centralwidget)
        self.reset_button.setObjectName(_fromUtf8("reset_button"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.FieldRole, self.reset_button)
        self.cancel_button = QtGui.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.FieldRole, self.cancel_button)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Pay Rate", None))
        self.label_2.setText(_translate("MainWindow", "Target Purchase", None))
        self.label_3.setText(_translate("MainWindow", "Work hours per week", None))
        self.ok_button.setText(_translate("MainWindow", "Ok", None))
        self.reset_button.setText(_translate("MainWindow", "Reset", None))
        self.cancel_button.setText(_translate("MainWindow", "Cancel", None))
        self.label_4.setText(_translate("MainWindow", "Days until Purchase", None))
        self.cancel_button.clicked.connect(self.close_window)
        self.reset_button.clicked.connect(self.reset_form)
        self.ok_button.clicked.connect(self.day_until_purchase_calculation)

    def close_window(self):
        sys.exit()
    def reset_form(self):
        self.pay_rate.setText(" ")
        self.target_purchase.setText(" ")
        self.per_month_pay.setValue(0)
        self.day_until_purchase.setText("")

    def day_until_purchase_calculation(self):
        payRate_value= float(self.pay_rate.text())
        perMonth_pay_value= float(self.per_month_pay.value())
        target_purchase_vale= float(self.target_purchase.text())
        week_count= 0
        while (target_purchase_vale > 0):
            target_purchase_vale -= (payRate_value * perMonth_pay_value)
            week_count+= 1
        if(week_count > 0):
            week_to_day= week_count * 7
            self.day_until_purchase.setText(str(week_to_day) )
        print (target_purchase_vale)
        print (week_count)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

