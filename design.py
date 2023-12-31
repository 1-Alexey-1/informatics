# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 800)
        MainWindow.setMinimumSize(QtCore.QSize(450, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.edt_text = QtWidgets.QTextEdit(self.centralwidget)
        self.edt_text.setObjectName("edt_text")
        self.verticalLayout.addWidget(self.edt_text)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(70, 70))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ext_btn = QtWidgets.QPushButton(self.groupBox)
        self.ext_btn.setMinimumSize(QtCore.QSize(140, 50))
        self.ext_btn.setStyleSheet("\n"
"QPushButton:hover{\n"
"    border-radius:6px;\n"
"     border:7px;\n"
"     \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.ext_btn.setObjectName("ext_btn")
        self.horizontalLayout.addWidget(self.ext_btn)
        self.save_bth = QtWidgets.QPushButton(self.groupBox)
        self.save_bth.setMinimumSize(QtCore.QSize(140, 50))
        self.save_bth.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:6px;\n"
"    background-color: rgb(215, 255, 67);\n"
"}")
        self.save_bth.setObjectName("save_bth")
        self.horizontalLayout.addWidget(self.save_bth)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.ext_btn.setText(_translate("MainWindow", "Exit"))
        self.save_bth.setText(_translate("MainWindow", "Save File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
