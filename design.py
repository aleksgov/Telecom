# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(760, 760)
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 230, 700, 350))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 35px; \n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.diagramButton1 = QtWidgets.QPushButton(self.widget)
        self.diagramButton1.setEnabled(True)
        self.diagramButton1.setGeometry(QtCore.QRect(70, 220, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.diagramButton1.setFont(font)
        self.diagramButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.diagramButton1.setMouseTracking(False)
        self.diagramButton1.setAutoFillBackground(False)
        self.diagramButton1.setStyleSheet("""
            QPushButton {
                background-color: rgb(88,176,226);
                color: white;
                border-radius: 7px;
            }
            QPushButton:hover {
                background-color: rgb(79,158,203);
            }
            QPushButton:pressed {
                background-color: rgb(97,193,248);
            }
        """)
        self.diagramButton1.setObjectName("diagramButton1")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(347, 20, 5, 315))
        self.widget_2.setStyleSheet("background-color: rgb(82,110,255);\n"
"border-radius: 2px;\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.CommonLabel = QtWidgets.QLabel(self.widget)
        self.CommonLabel.setGeometry(QtCore.QRect(20, 20, 300, 50))
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
        self.diagramButton2.setGeometry(QtCore.QRect(430, 260, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.diagramButton2.setFont(font)
        self.diagramButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.diagramButton2.setMouseTracking(False)
        self.diagramButton2.setAutoFillBackground(False)
        self.diagramButton2.setStyleSheet("""
            QPushButton {
                background-color: rgb(88,176,226);
                color: white;
                border-radius: 7px;
            }
            QPushButton:hover {
                background-color: rgb(79,158,203);
            }
            QPushButton:pressed {
                background-color: rgb(97,193,248);
            }
        """)
        self.diagramButton2.setObjectName("diagramButton2")
        self.fileButton1 = QtWidgets.QPushButton(self.widget)
        self.fileButton1.setEnabled(True)
        self.fileButton1.setGeometry(QtCore.QRect(110, 110, 120, 70))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fileButton1.setFont(font)
        self.fileButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileButton1.setMouseTracking(False)
        self.fileButton1.setAutoFillBackground(False)
        self.fileButton1.setStyleSheet("""
    QPushButton {
        border: 2px solid rgb(146,146,146);
        border-radius: 10px;
        background-color: rgb(255, 255, 255);
    }
    QPushButton:hover {
        background-color: rgb(240, 240, 240);
    }
    QPushButton:pressed {
        background-color: rgb(230, 230, 230);
    }
""")
        self.fileButton1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileButton1.setIcon(icon)
        self.fileButton1.setIconSize(QtCore.QSize(60, 60))
        self.fileButton1.setObjectName("fileButton1")
        self.fileButton2 = QtWidgets.QPushButton(self.widget)
        self.fileButton2.setEnabled(True)
        self.fileButton2.setGeometry(QtCore.QRect(470, 165, 120, 70))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fileButton2.setFont(font)
        self.fileButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileButton2.setMouseTracking(False)
        self.fileButton2.setAutoFillBackground(False)
        self.fileButton2.setStyleSheet("""
    QPushButton {
        border: 2px solid rgb(146,146,146);
        border-radius: 10px;
        background-color: rgb(255, 255, 255);
    }
    QPushButton:hover {
        background-color: rgb(240, 240, 240);
    }
    QPushButton:pressed {
        background-color: rgb(230, 230, 230);
    }
""")
        self.fileButton2.setText("")
        self.fileButton2.setIcon(icon)
        self.fileButton2.setIconSize(QtCore.QSize(60, 60))
        self.fileButton2.setObjectName("fileButton2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 100, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setToolTip("")
        self.lineEdit.setStyleSheet("color: rgb(146,146,146);\n"
"\n"
"\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.IndividualLabel_2 = QtWidgets.QLabel(self.widget)
        self.IndividualLabel_2.setGeometry(QtCore.QRect(380, 90, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IndividualLabel_2.sizePolicy().hasHeightForWidth())
        self.IndividualLabel_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.IndividualLabel_2.setFont(font)
        self.IndividualLabel_2.setStyleSheet("border: 2px solid rgb(146,146,146);\n"
"color: rgb(146,146,146);\n"
"border-radius: 12px;")
        self.IndividualLabel_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IndividualLabel_2.setText("")
        self.IndividualLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.IndividualLabel_2.setObjectName("IndividualLabel_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(390, 100, 41, 31))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images\\loupe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.IndividualLabel_2.raise_()
        self.diagramButton1.raise_()
        self.widget_2.raise_()
        self.CommonLabel.raise_()
        self.IndividualLabel.raise_()
        self.diagramButton2.raise_()
        self.fileButton1.raise_()
        self.fileButton2.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setEnabled(True)
        self.changeButton.setGeometry(QtCore.QRect(100, 620, 550, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.changeButton.setFont(font)
        self.changeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeButton.setMouseTracking(False)
        self.changeButton.setAutoFillBackground(False)
        self.changeButton.setStyleSheet("""
    QPushButton {
        background-color: rgb(30, 74, 163);
        color: white;
        border-radius: 7px;
    }
    QPushButton:hover {
        background-color: rgb(27, 66, 146);
    }
    QPushButton:pressed {
        background-color: rgb(33, 81, 179);
    }
""")
        self.changeButton.setObjectName("changeButton")
        self.fileButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton3.setEnabled(True)
        self.fileButton3.setGeometry(QtCore.QRect(270, 130, 220, 70))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fileButton3.setFont(font)
        self.fileButton3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileButton3.setMouseTracking(False)
        self.fileButton3.setAutoFillBackground(False)
        self.fileButton3.setStyleSheet("""
    QPushButton {
        border: 2px solid rgb(146,146,146);
        border-radius: 10px;
        background-color: rgb(255, 255, 255);
    }
    QPushButton:hover {
        background-color: rgb(240, 240, 240);
    }
    QPushButton:pressed {
        background-color: rgb(230, 230, 230);
    }
""")
        self.fileButton3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images\\file+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileButton3.setIcon(icon2)
        self.fileButton3.setIconSize(QtCore.QSize(52, 52))
        self.fileButton3.setObjectName("fileButton3")
        self.fileLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileLabel.setGeometry(QtCore.QRect(200, 40, 360, 55))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileLabel.sizePolicy().hasHeightForWidth())
        self.fileLabel.setSizePolicy(sizePolicy)
        self.fileLabel.setBaseSize(QtCore.QSize(700, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.fileLabel.setFont(font)
        self.fileLabel.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.fileLabel.setStyleSheet("background-color: rgb(91,145,250); color: white; border-radius: 7px;")
        self.fileLabel.setTextFormat(QtCore.Qt.RichText)
        self.fileLabel.setScaledContents(True)
        self.fileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileLabel.setWordWrap(False)
        self.fileLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.fileLabel.setObjectName("fileLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
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
        self.diagramButton1.setText(_translate("MainWindow", "ДИАГРАММА"))
        self.CommonLabel.setText(_translate("MainWindow", "ОБЩИЙ"))
        self.IndividualLabel.setText(_translate("MainWindow", "ИНДИВИДУАЛЬНЫЙ"))
        self.diagramButton2.setText(_translate("MainWindow", "ДИАГРАММА"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите ФИО"))
        self.changeButton.setText(_translate("MainWindow", "ДОБАВИТЬ/ИЗМЕНИТЬ СПИСОК РАБОТНИКОВ"))
        self.fileLabel.setText(_translate("MainWindow", "ЗАГРУЗИТЕ ФАЙЛ"))
