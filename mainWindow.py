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
        self.v_artistListWidget = QtWidgets.QVBoxLayout()
        self.v_artistListWidget.setContentsMargins(0, -1, -1, -1)
        self.v_artistListWidget.setSpacing(6)
        self.v_artistListWidget.setObjectName("v_artistListWidget")
        self.searchEdit = QtWidgets.QLineEdit(self.h_mainWidget)
        self.searchEdit.setText("")
        self.searchEdit.setObjectName("searchEdit")
        self.v_artistListWidget.addWidget(self.searchEdit)
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
        self.v_artistListWidget.addWidget(self.listViewArtists)
        self.horizontalLayout.addLayout(self.v_artistListWidget)
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
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelArtist = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelArtist.sizePolicy().hasHeightForWidth())
        self.labelArtist.setSizePolicy(sizePolicy)
        self.labelArtist.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelArtist.setFont(font)
        self.labelArtist.setAutoFillBackground(False)
        self.labelArtist.setFrameShape(QtWidgets.QFrame.Box)
        self.labelArtist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labelArtist.setLineWidth(1)
        self.labelArtist.setMidLineWidth(0)
        self.labelArtist.setTextFormat(QtCore.Qt.RichText)
        self.labelArtist.setScaledContents(True)
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
        self.tableWidgetAlbums.setMinimumSize(QtCore.QSize(50, 0))
        self.tableWidgetAlbums.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidgetAlbums.setAutoScrollMargin(16)
        self.tableWidgetAlbums.setProperty("showDropIndicator", False)
        self.tableWidgetAlbums.setDragDropOverwriteMode(False)
        self.tableWidgetAlbums.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetAlbums.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.cover = QtWidgets.QLabel(self.v_albumWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cover.sizePolicy().hasHeightForWidth())
        self.cover.setSizePolicy(sizePolicy)
        self.cover.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cover.setText("")
        self.cover.setAlignment(QtCore.Qt.AlignCenter)
        self.cover.setObjectName("cover")
        self.gridLayout_5.addWidget(self.cover, 0, 0, 1, 1)
        self.tableWidgetTracks = QtWidgets.QTableWidget(self.v_albumWidget)
        self.tableWidgetTracks.setMinimumSize(QtCore.QSize(50, 0))
        self.tableWidgetTracks.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetTracks.setObjectName("tableWidgetTracks")
        self.tableWidgetTracks.setColumnCount(3)
        self.tableWidgetTracks.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetTracks.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetTracks.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetTracks.setHorizontalHeaderItem(2, item)
        self.gridLayout_5.addWidget(self.tableWidgetTracks, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playButton = QtWidgets.QPushButton(self.v_albumWidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_2.addWidget(self.playButton)
        self.stopButton = QtWidgets.QPushButton(self.v_albumWidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.previousButton = QtWidgets.QPushButton(self.v_albumWidget)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_2.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(self.v_albumWidget)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.openDirButton = QtWidgets.QPushButton(self.v_albumWidget)
        self.openDirButton.setObjectName("openDirButton")
        self.horizontalLayout_2.addWidget(self.openDirButton)
        self.volumeSlider = QtWidgets.QSlider(self.v_albumWidget)
        self.volumeSlider.setMinimumSize(QtCore.QSize(100, 17))
        self.volumeSlider.setMaximumSize(QtCore.QSize(100, 17))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_2.addWidget(self.volumeSlider)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
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
        self.actionRandom_album = QtWidgets.QAction(MainWindow)
        self.actionRandom_album.setObjectName("actionRandom_album")
        self.menuConfiguration.addAction(self.actionMusic_directories)
        self.menuConfiguration.addAction(self.actionExplore_music_directories)
        self.menuConfiguration.addAction(self.actionDelete_database)
        self.menuConfiguration.addAction(self.actionRandom_album)
        self.menuBar.addAction(self.menuConfiguration.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchEdit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.labelArtist.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Artist</span></p><p><span style=\" font-style:italic;\">Album Name (1970)</span></p></body></html>"))
        item = self.tableWidgetAlbums.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidgetAlbums.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Year"))
        item = self.tableWidgetAlbums.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidgetTracks.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidgetTracks.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.tableWidgetTracks.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.previousButton.setText(_translate("MainWindow", "<<"))
        self.nextButton.setText(_translate("MainWindow", ">>"))
        self.openDirButton.setText(_translate("MainWindow", "Open Dir"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Config"))
        self.actionMusic_directories.setText(_translate("MainWindow", "Music directories"))
        self.actionExplore_music_directories.setText(_translate("MainWindow", "Explore music directories"))
        self.actionDelete_database.setText(_translate("MainWindow", "Delete database"))
        self.actionRandom_album.setText(_translate("MainWindow", "Random album"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

