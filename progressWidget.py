#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class progressWidget(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.initUI()

    def initUI(self):

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(0, 0, 250, 20)
        self.progress.setValue(0)
        self.directory = QtWidgets.QLabel('Directory', self)
        #self.directory.move(0, 30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        self.directory.setSizePolicy(sizePolicy)
        self.directory.setGeometry(0, 30, 250, 20)
        self.show()

    def setValue(self,value):
        self.progress.setValue(value)
        self.setWindowTitle(str(value)+"%")

    def setDirectoryText(self,value):
        self.directory.setText(value)