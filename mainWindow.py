# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.ForceTabbedDocks)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.h_mainWidget = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.h_mainWidget.sizePolicy().hasHeightForWidth())
        self.h_mainWidget.setSizePolicy(sizePolicy)
        self.h_mainWidget.setObjectName("h_mainWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.h_mainWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listViewArtists = QtWidgets.QListView(self.h_mainWidget)
        self.listViewArtists.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.listViewArtists.sizePolicy().hasHeightForWidth())
        self.listViewArtists.setSizePolicy(sizePolicy)
        self.listViewArtists.setMinimumSize(QtCore.QSize(150, 0))
        self.listViewArtists.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewArtists.setProperty("showDropIndicator", False)
        self.listViewArtists.setResizeMode(QtWidgets.QListView.Adjust)
        self.listViewArtists.setObjectName("listViewArtists")
        self.horizontalLayout.addWidget(self.listViewArtists)
        self.v_artistWidget = QtWidgets.QWidget(self.h_mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.v_artistWidget.sizePolicy().hasHeightForWidth())
        self.v_artistWidget.setSizePolicy(sizePolicy)
        self.v_artistWidget.setObjectName("v_artistWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.v_artistWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget = QtWidgets.QWidget(self.v_artistWidget)
        self.verticalWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.verticalWidget.setObjectName("verticalWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.verticalWidget)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelArtist = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelArtist.sizePolicy().hasHeightForWidth())
        self.labelArtist.setSizePolicy(sizePolicy)
        self.labelArtist.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelArtist.setFont(font)
        self.labelArtist.setAlignment(QtCore.Qt.AlignCenter)
        self.labelArtist.setObjectName("labelArtist")
        self.gridLayout_6.addWidget(self.labelArtist, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.verticalWidget)
        self.h_albumsWidget = QtWidgets.QWidget(self.v_artistWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.h_albumsWidget.sizePolicy().hasHeightForWidth())
        self.h_albumsWidget.setSizePolicy(sizePolicy)
        self.h_albumsWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.h_albumsWidget.setObjectName("h_albumsWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.h_albumsWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidgetAlbums = QtWidgets.QTableWidget(self.h_albumsWidget)
        self.tableWidgetAlbums.setEnabled(True)
        self.tableWidgetAlbums.setAutoScrollMargin(16)
        self.tableWidgetAlbums.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetAlbums.setColumnCount(3)
        self.tableWidgetAlbums.setObjectName("tableWidgetAlbums")
        self.tableWidgetAlbums.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAlbums.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAlbums.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAlbums.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_3.addWidget(self.tableWidgetAlbums)
        self.v_albumWidget = QtWidgets.QWidget(self.h_albumsWidget)
        self.v_albumWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.v_albumWidget.setObjectName("v_albumWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.v_albumWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.stopButton = QtWidgets.QPushButton(self.v_albumWidget)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_5.addWidget(self.stopButton, 2, 0, 1, 1)
        self.tableWidgetTracks = QtWidgets.QTableWidget(self.v_albumWidget)
        self.tableWidgetTracks.setObjectName("tableWidgetTracks")
        self.tableWidgetTracks.setColumnCount(0)
        self.tableWidgetTracks.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidgetTracks, 4, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.v_albumWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.playButton = QtWidgets.QPushButton(self.v_albumWidget)
        self.playButton.setObjectName("playButton")
        self.gridLayout_5.addWidget(self.playButton, 1, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.v_albumWidget)
        self.verticalLayout.addWidget(self.h_albumsWidget)
        self.horizontalLayout.addWidget(self.v_artistWidget)
        self.gridLayout.addWidget(self.h_mainWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuConfiguration = QtWidgets.QMenu(self.menuBar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionMusic_directories = QtWidgets.QAction(MainWindow)
        self.actionMusic_directories.setObjectName("actionMusic_directories")
        self.actionExplore_music_directories = QtWidgets.QAction(MainWindow)
        self.actionExplore_music_directories.setObjectName("actionExplore_music_directories")
        self.actionDelete_database = QtWidgets.QAction(MainWindow)
        self.actionDelete_database.setObjectName("actionDelete_database")
        self.menuConfiguration.addAction(self.actionMusic_directories)
        self.menuConfiguration.addAction(self.actionExplore_music_directories)
        self.menuConfiguration.addAction(self.actionDelete_database)
        self.menuBar.addAction(self.menuConfiguration.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelArtist.setText(_translate("MainWindow", "Artist"))
        item = self.tableWidgetAlbums.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidgetAlbums.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Year"))
        item = self.tableWidgetAlbums.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Config"))
        self.actionMusic_directories.setText(_translate("MainWindow", "Music directories"))
        self.actionExplore_music_directories.setText(_translate("MainWindow", "Explore Music directories"))
        self.actionDelete_database.setText(_translate("MainWindow", "Delete database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

