# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AutoClicker(object):
    def setupUi(self, AutoClicker):
        AutoClicker.setObjectName("AutoClicker")
        AutoClicker.setEnabled(True)
        AutoClicker.resize(383, 136)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AutoClicker.sizePolicy().hasHeightForWidth())
        AutoClicker.setSizePolicy(sizePolicy)
        AutoClicker.setMinimumSize(QtCore.QSize(383, 136))
        AutoClicker.setMaximumSize(QtCore.QSize(383, 136))
        AutoClicker.setStyleSheet("background:black;color:#bfbfbf;")
        self.centralwidget = QtWidgets.QWidget(AutoClicker)
        self.centralwidget.setObjectName("centralwidget")
        self.ToggleButton = QtWidgets.QPushButton(self.centralwidget)
        self.ToggleButton.setGeometry(QtCore.QRect(10, 40, 111, 71))
        self.ToggleButton.setStyleSheet("background:#1c1c1c")
        self.ToggleButton.setObjectName("ToggleButton")
        self.PressText = QtWidgets.QLineEdit(self.centralwidget)
        self.PressText.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.PressText.setStyleSheet("QLineEdit{background:#1c1c1c;}QLineEdit:disabled{background:#555;color:#888}")
        self.PressText.setObjectName("PressText")
        self.TriggerText = QtWidgets.QLineEdit(self.centralwidget)
        self.TriggerText.setGeometry(QtCore.QRect(260, 40, 113, 20))
        self.TriggerText.setStyleSheet("QLineEdit{background:#1c1c1c;}QLineEdit:disabled{background:#333}")
        self.TriggerText.setObjectName("TriggerText")
        self.LeftClick = QtWidgets.QCheckBox(self.centralwidget)
        self.LeftClick.setEnabled(True)
        self.LeftClick.setGeometry(QtCore.QRect(130, 60, 81, 21))
        self.LeftClick.setChecked(True)
        self.LeftClick.setObjectName("LeftClick")
        self.RightClick = QtWidgets.QCheckBox(self.centralwidget)
        self.RightClick.setEnabled(True)
        self.RightClick.setGeometry(QtCore.QRect(130, 80, 81, 16))
        self.RightClick.setChecked(False)
        self.RightClick.setObjectName("RightClick")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.OnOff = QtWidgets.QLabel(self.centralwidget)
        self.OnOff.setGeometry(QtCore.QRect(30, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.OnOff.setFont(font)
        self.OnOff.setObjectName("OnOff")
        AutoClicker.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AutoClicker)
        self.statusbar.setObjectName("statusbar")
        AutoClicker.setStatusBar(self.statusbar)

        self.retranslateUi(AutoClicker)
        QtCore.QMetaObject.connectSlotsByName(AutoClicker)

    def retranslateUi(self, AutoClicker):
        _translate = QtCore.QCoreApplication.translate
        AutoClicker.setWindowTitle(_translate("AutoClicker", "AutoClicker"))
        self.ToggleButton.setText(_translate("AutoClicker", "Toggle"))
        self.PressText.setText(_translate("AutoClicker", "space"))
        self.TriggerText.setText(_translate("AutoClicker", "ctrl+shift"))
        self.LeftClick.setText(_translate("AutoClicker", "Left Click"))
        self.RightClick.setText(_translate("AutoClicker", "Right Click"))
        self.label.setText(_translate("AutoClicker", "Output"))
        self.label_2.setText(_translate("AutoClicker", "Toggle Key"))
        self.OnOff.setText(_translate("AutoClicker", "OFF"))
