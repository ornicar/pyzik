# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 608)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.h_mainWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.h_mainWidget)
        self.splitter.setLineWidth(6)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.v_ArtistSelector = QtWidgets.QWidget(self.splitter)
        self.v_ArtistSelector.setObjectName("v_ArtistSelector")
        self.v_artistListWidget = QtWidgets.QVBoxLayout(self.v_ArtistSelector)
        self.v_artistListWidget.setContentsMargins(1, 0, 0, 0)
        self.v_artistListWidget.setSpacing(6)
        self.v_artistListWidget.setObjectName("v_artistListWidget")
        self.searchEdit = QtWidgets.QLineEdit(self.v_ArtistSelector)
        self.searchEdit.setText("")
        self.searchEdit.setObjectName("searchEdit")
        self.v_artistListWidget.addWidget(self.searchEdit)
        self.listViewArtists = QtWidgets.QListView(self.v_ArtistSelector)
        self.listViewArtists.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.listViewArtists.sizePolicy().hasHeightForWidth())
        self.listViewArtists.setSizePolicy(sizePolicy)
        self.listViewArtists.setMinimumSize(QtCore.QSize(150, 0))
        self.listViewArtists.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listViewArtists.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listViewArtists.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewArtists.setProperty("showDropIndicator", False)
        self.listViewArtists.setResizeMode(QtWidgets.QListView.Adjust)
        self.listViewArtists.setObjectName("listViewArtists")
        self.v_artistListWidget.addWidget(self.listViewArtists)
        self.v_artistWidget = QtWidgets.QWidget(self.splitter)
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
        self.verticalWidget.setMaximumSize(QtCore.QSize(16777215, 80))
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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.h_albumsWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitterArtist = QtWidgets.QSplitter(self.h_albumsWidget)
        self.splitterArtist.setLineWidth(6)
        self.splitterArtist.setOrientation(QtCore.Qt.Horizontal)
        self.splitterArtist.setObjectName("splitterArtist")
        self.tableWidgetAlbums = QtWidgets.QTableWidget(self.splitterArtist)
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
        self.v_albumWidget = QtWidgets.QWidget(self.splitterArtist)
        self.v_albumWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.v_albumWidget.setObjectName("v_albumWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.v_albumWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitterAlbum = QtWidgets.QSplitter(self.v_albumWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitterAlbum.sizePolicy().hasHeightForWidth())
        self.splitterAlbum.setSizePolicy(sizePolicy)
        self.splitterAlbum.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.splitterAlbum.setLineWidth(6)
        self.splitterAlbum.setOrientation(QtCore.Qt.Vertical)
        self.splitterAlbum.setOpaqueResize(True)
        self.splitterAlbum.setObjectName("splitterAlbum")
        self.coverWidget = QtWidgets.QWidget(self.splitterAlbum)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.coverWidget.sizePolicy().hasHeightForWidth())
        self.coverWidget.setSizePolicy(sizePolicy)
        self.coverWidget.setMinimumSize(QtCore.QSize(100, 100))
        self.coverWidget.setObjectName("coverWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.coverWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cover = QtWidgets.QLabel(self.coverWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.cover.sizePolicy().hasHeightForWidth())
        self.cover.setSizePolicy(sizePolicy)
        self.cover.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cover.setText("")
        self.cover.setAlignment(QtCore.Qt.AlignCenter)
        self.cover.setObjectName("cover")
        self.gridLayout_5.addWidget(self.cover, 0, 0, 1, 1)
        self.tracksWidget = QtWidgets.QWidget(self.splitterAlbum)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tracksWidget.sizePolicy().hasHeightForWidth())
        self.tracksWidget.setSizePolicy(sizePolicy)
        self.tracksWidget.setObjectName("tracksWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tracksWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.h_playerButtons = QtWidgets.QWidget(self.tracksWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.h_playerButtons.sizePolicy().hasHeightForWidth())
        self.h_playerButtons.setSizePolicy(sizePolicy)
        self.h_playerButtons.setMinimumSize(QtCore.QSize(0, 40))
        self.h_playerButtons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.h_playerButtons.setObjectName("h_playerButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.h_playerButtons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalWidget = QtWidgets.QWidget(self.h_playerButtons)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(0, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_2.addWidget(self.playButton)
        self.openDirButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.openDirButton.setObjectName("openDirButton")
        self.horizontalLayout_2.addWidget(self.openDirButton)
        self.nextButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.previousButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_2.addWidget(self.previousButton)
        self.stopButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.horizontalLayout.addWidget(self.horizontalWidget)
        self.volumeSlider = QtWidgets.QSlider(self.h_playerButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(sizePolicy)
        self.volumeSlider.setMinimumSize(QtCore.QSize(60, 0))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout.addWidget(self.volumeSlider)
        self.verticalLayout_2.addWidget(self.h_playerButtons)
        self.tableWidgetTracks = QtWidgets.QTableWidget(self.tracksWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidgetTracks.sizePolicy().hasHeightForWidth())
        self.tableWidgetTracks.setSizePolicy(sizePolicy)
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
        self.verticalLayout_2.addWidget(self.tableWidgetTracks)
        self.verticalLayout_3.addWidget(self.splitterAlbum)
        self.gridLayout_4.addWidget(self.splitterArtist, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.h_albumsWidget)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.h_mainWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 854, 27))
        self.menuBar.setObjectName("menuBar")
        self.menuConfiguration = QtWidgets.QMenu(self.menuBar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        self.menuRadios = QtWidgets.QMenu(self.menuBar)
        self.menuRadios.setObjectName("menuRadios")
        self.menuAlbums = QtWidgets.QMenu(self.menuBar)
        self.menuAlbums.setObjectName("menuAlbums")
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
        self.actionFuzzyGroovy = QtWidgets.QAction(MainWindow)
        self.actionFuzzyGroovy.setObjectName("actionFuzzyGroovy")
        self.menuConfiguration.addAction(self.actionMusic_directories)
        self.menuConfiguration.addAction(self.actionExplore_music_directories)
        self.menuConfiguration.addAction(self.actionDelete_database)
        self.menuRadios.addAction(self.actionFuzzyGroovy)
        self.menuAlbums.addAction(self.actionRandom_album)
        self.menuBar.addAction(self.menuConfiguration.menuAction())
        self.menuBar.addAction(self.menuAlbums.menuAction())
        self.menuBar.addAction(self.menuRadios.menuAction())

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
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.openDirButton.setText(_translate("MainWindow", "Open Dir"))
        self.nextButton.setText(_translate("MainWindow", ">>"))
        self.previousButton.setText(_translate("MainWindow", "<<"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        item = self.tableWidgetTracks.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidgetTracks.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.tableWidgetTracks.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Config"))
        self.menuRadios.setTitle(_translate("MainWindow", "Radios"))
        self.menuAlbums.setTitle(_translate("MainWindow", "Albums"))
        self.actionMusic_directories.setText(_translate("MainWindow", "Music directories"))
        self.actionExplore_music_directories.setText(_translate("MainWindow", "Explore music directories"))
        self.actionDelete_database.setText(_translate("MainWindow", "Delete database"))
        self.actionRandom_album.setText(_translate("MainWindow", "Random album"))
        self.actionFuzzyGroovy.setText(_translate("MainWindow", "Fuzzy and Groovy Rock Radio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

