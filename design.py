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
        MainWindow.resize(400, 100)
        MainWindow.setMinimumSize(QtCore.QSize(400, 100))
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.dayTempLabel = QtWidgets.QLabel(self.widget)
        self.dayTempLabel.setObjectName("dayTempLabel")
        self.gridLayout.addWidget(self.dayTempLabel, 2, 2, 1, 1)
        self.dayTempSlider = QtWidgets.QSlider(self.widget)
        self.dayTempSlider.setOrientation(QtCore.Qt.Horizontal)
        self.dayTempSlider.setObjectName("dayTempSlider")
        self.gridLayout.addWidget(self.dayTempSlider, 2, 1, 1, 1)
        self.stateCheckBox = QtWidgets.QCheckBox(self.widget)
        self.stateCheckBox.setObjectName("stateCheckBox")
        self.gridLayout.addWidget(self.stateCheckBox, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dayTempLabel.setText(_translate("MainWindow", "6500"))
        self.stateCheckBox.setText(_translate("MainWindow", "Enabled"))
        self.label.setText(_translate("MainWindow", "K"))

