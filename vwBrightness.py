# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vwBrightness.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(767, 757)
        self.brightnessSlider = QtWidgets.QSlider(Dialog)
        self.brightnessSlider.setGeometry(QtCore.QRect(50, 390, 369, 31))
        self.brightnessSlider.setMaximum(100)
        self.brightnessSlider.setProperty("value", 50)
        self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.brightnessSlider.setTickInterval(1)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.brightnessSpin = QtWidgets.QSpinBox(Dialog)
        self.brightnessSpin.setGeometry(QtCore.QRect(50, 580, 81, 41))
        self.brightnessSpin.setMaximum(100)
        self.brightnessSpin.setProperty("value", 50)
        self.brightnessSpin.setObjectName("brightnessSpin")
        self.takePhoto = QtWidgets.QPushButton(Dialog)
        self.takePhoto.setGeometry(QtCore.QRect(50, 100, 99, 30))
        self.takePhoto.setObjectName("takePhoto")
        self.startRecord = QtWidgets.QPushButton(Dialog)
        self.startRecord.setGeometry(QtCore.QRect(50, 140, 99, 30))
        self.startRecord.setObjectName("startRecord")
        self.stopRecord = QtWidgets.QPushButton(Dialog)
        self.stopRecord.setGeometry(QtCore.QRect(50, 180, 99, 30))
        self.stopRecord.setObjectName("stopRecord")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 340, 188, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.brightnessDial = QtWidgets.QDial(Dialog)
        self.brightnessDial.setGeometry(QtCore.QRect(50, 440, 100, 100))
        self.brightnessDial.setMaximum(100)
        self.brightnessDial.setProperty("value", 50)
        self.brightnessDial.setNotchesVisible(True)
        self.brightnessDial.setObjectName("brightnessDial")
        self.Preview = QtWidgets.QLabel(Dialog)
        self.Preview.setGeometry(QtCore.QRect(50, 240, 58, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Preview.setFont(font)
        self.Preview.setObjectName("Preview")
        self.preview = QtWidgets.QCheckBox(Dialog)
        self.preview.setGeometry(QtCore.QRect(130, 240, 101, 27))
        self.preview.setChecked(True)
        self.preview.setObjectName("preview")
        self.Preview.setBuddy(self.Preview)

        self.retranslateUi(Dialog)
        self.takePhoto.clicked.connect(Dialog.takePhoto)
        self.startRecord.clicked.connect(Dialog.startRecording)
        self.stopRecord.clicked.connect(Dialog.stopRecording)
        self.brightnessSlider.valueChanged['int'].connect(Dialog.changeBrightness)
        self.brightnessDial.sliderMoved['int'].connect(Dialog.changeBrightness)
        self.brightnessSpin.valueChanged['int'].connect(Dialog.changeBrightness)
        self.preview.clicked['bool'].connect(Dialog.showPreview)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.takePhoto.setText(_translate("Dialog", "Take Photo"))
        self.startRecord.setText(_translate("Dialog", "Start Rec"))
        self.stopRecord.setText(_translate("Dialog", "Stop Rec"))
        self.label.setText(_translate("Dialog", "Adjust Camera Brightness"))
        self.Preview.setText(_translate("Dialog", "Preview"))
        self.preview.setText(_translate("Dialog", "CheckBox"))

