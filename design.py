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
        MainWindow.setEnabled(True)
        MainWindow.resize(750, 750)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(222,241,255);\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setEnabled(True)
        self.fileButton.setGeometry(QtCore.QRect(200, 50, 350, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fileButton.setFont(font)
        self.fileButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.fileButton.setMouseTracking(False)
        self.fileButton.setAutoFillBackground(False)
        self.fileButton.setStyleSheet("border: none;\n"
"border-radius: 0px;\n"
"background-color: rgb(91,145,250); \n"
"color: white;\n"
"border-radius: 7px;")
        self.fileButton.setObjectName("fileButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(25, 250, 700, 350))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 35px; \n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.diagramButton1 = QtWidgets.QPushButton(self.widget)
        self.diagramButton1.setEnabled(True)
        self.diagramButton1.setGeometry(QtCore.QRect(80, 240, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.diagramButton1.setFont(font)
        self.diagramButton1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.diagramButton1.setMouseTracking(False)
        self.diagramButton1.setAutoFillBackground(False)
        self.diagramButton1.setStyleSheet("background-color: rgb(88,176,226);\n"
"color: white;\n"
"border-radius: 7px;")
        self.diagramButton1.setObjectName("diagramButton1")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(350, 20, 5, 315))
        self.widget_2.setStyleSheet("background-color: rgb(82,110,255)\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.CommonLabel = QtWidgets.QLabel(self.widget)
        self.CommonLabel.setGeometry(QtCore.QRect(25, 20, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CommonLabel.sizePolicy().hasHeightForWidth())
        self.CommonLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.CommonLabel.setFont(font)
        self.CommonLabel.setStyleSheet("background-color: rgb(91,145,250); \n"
"color: white;\n"
"border-radius: 7px;")
        self.CommonLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CommonLabel.setObjectName("CommonLabel")
        self.IndividualLabel = QtWidgets.QLabel(self.widget)
        self.IndividualLabel.setGeometry(QtCore.QRect(380, 20, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IndividualLabel.sizePolicy().hasHeightForWidth())
        self.IndividualLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.IndividualLabel.setFont(font)
        self.IndividualLabel.setStyleSheet("background-color: rgb(91,145,250); \n"
"color: white;\n"
"border-radius: 7px;")
        self.IndividualLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IndividualLabel.setObjectName("IndividualLabel")
        self.diagramButton2 = QtWidgets.QPushButton(self.widget)
        self.diagramButton2.setEnabled(True)
        self.diagramButton2.setGeometry(QtCore.QRect(430, 240, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.diagramButton2.setFont(font)
        self.diagramButton2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.diagramButton2.setMouseTracking(False)
        self.diagramButton2.setAutoFillBackground(False)
        self.diagramButton2.setStyleSheet("background-color: rgb(88,176,226);\n"
"color: white;\n"
"border-radius: 7px;")
        self.diagramButton2.setObjectName("diagramButton2")
        self.diagramButton1_2 = QtWidgets.QPushButton(self.widget)
        self.diagramButton1_2.setEnabled(True)
        self.diagramButton1_2.setGeometry(QtCore.QRect(130, 130, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.diagramButton1_2.setFont(font)
        self.diagramButton1_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.diagramButton1_2.setMouseTracking(False)
        self.diagramButton1_2.setAutoFillBackground(False)
        self.diagramButton1_2.setStyleSheet("box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5);\n"
"")
        self.diagramButton1_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/free-icon-file-2745398.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.diagramButton1_2.setIcon(icon)
        self.diagramButton1_2.setIconSize(QtCore.QSize(64, 64))
        self.diagramButton1_2.setObjectName("diagramButton1_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
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
        self.fileButton.setText(_translate("MainWindow", "ЗАГРУЗИТЕ ФАЙЛ"))
        self.diagramButton1.setText(_translate("MainWindow", "ДИАГРАММА"))
        self.CommonLabel.setText(_translate("MainWindow", "ОБЩИЙ"))
        self.IndividualLabel.setText(_translate("MainWindow", "ОБЩИЙ"))
        self.diagramButton2.setText(_translate("MainWindow", "ДИАГРАММА"))
