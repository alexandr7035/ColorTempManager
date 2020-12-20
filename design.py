# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 119)
        MainWindow.setMinimumSize(QtCore.QSize(400, 100))
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.stateCheckBox = QtWidgets.QCheckBox(self.widget)
        self.stateCheckBox.setObjectName("stateCheckBox")
        self.gridLayout.addWidget(self.stateCheckBox, 4, 0, 1, 1)
        self.dayTempSlider = QtWidgets.QSlider(self.widget)
        self.dayTempSlider.setOrientation(QtCore.Qt.Horizontal)
        self.dayTempSlider.setObjectName("dayTempSlider")
        self.gridLayout.addWidget(self.dayTempSlider, 2, 1, 1, 1)
        self.settingsBtn = QtWidgets.QPushButton(self.widget)
        self.settingsBtn.setObjectName("settingsBtn")
        self.gridLayout.addWidget(self.settingsBtn, 4, 1, 1, 1)
        self.dayText = QtWidgets.QLabel(self.widget)
        self.dayText.setObjectName("dayText")
        self.gridLayout.addWidget(self.dayText, 2, 0, 1, 1)
        self.nightTempSlider = QtWidgets.QSlider(self.widget)
        self.nightTempSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nightTempSlider.setObjectName("nightTempSlider")
        self.gridLayout.addWidget(self.nightTempSlider, 3, 1, 1, 1)
        self.nightText = QtWidgets.QLabel(self.widget)
        self.nightText.setObjectName("nightText")
        self.gridLayout.addWidget(self.nightText, 3, 0, 1, 1)
        self.dayTempLabel = QtWidgets.QLabel(self.widget)
        self.dayTempLabel.setObjectName("dayTempLabel")
        self.gridLayout.addWidget(self.dayTempLabel, 2, 2, 1, 1)
        self.nightTempLabel = QtWidgets.QLabel(self.widget)
        self.nightTempLabel.setObjectName("nightTempLabel")
        self.gridLayout.addWidget(self.nightTempLabel, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stateCheckBox.setText(_translate("MainWindow", "Enabled"))
        self.settingsBtn.setText(_translate("MainWindow", "Settings"))
        self.dayText.setText(_translate("MainWindow", "Day"))
        self.nightText.setText(_translate("MainWindow", "Night"))
        self.dayTempLabel.setText(_translate("MainWindow", "6500"))
        self.nightTempLabel.setText(_translate("MainWindow", "1000"))

