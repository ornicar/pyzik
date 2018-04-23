#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, subprocess
from PyQt5 import QtWidgets, QtGui, QtCore
import mainWindow  # import of mainWindow.py made with pyuic5
from musicBase import *
from musicDirectory import *
from database import *
from playerVLC import *
from darkStyle import darkStyle
from dialogMusicDirectoriesLoader import *
from streamObserver import *
from albumThread import *
from musicBaseThread import *
from playlistWidget import *



def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])



class MainWindowLoader(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

       
        self.currentArtist = artist("",0)
        self.currentAlbum = album("")
        self.coverPixmap = QtGui.QPixmap()
        self.defaultPixmap = QtGui.QPixmap()
        self.firstShow = True
        self.playList = None

        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setTitleLabel("")
        self.setWindowTitle("PyZik")
        self.initAlbumTableWidget()
        self.initTrackTableWidget()

        self.showArtists()
        

        #Connect UI triggers
        self.ui.listViewArtists.selectionModel().currentChanged.connect(self.onArtistChange)
        #self.ui.listViewArtists.selectionModel().currentRowChanged.connect(self.onArtistChange)
        #self.ui.listViewArtists.clicked.connect(self.onArtistChange)
        self.ui.actionMusic_directories.triggered.connect(self.onMenuMusicDirectories)
        self.ui.actionExplore_music_directories.triggered.connect(self.onMenuExplore)
        self.ui.actionRandom_album.triggered.connect(self.ramdomAlbum)
        self.ui.actionDelete_database.triggered.connect(self.onMenuDeleteDatabase)
        self.ui.actionFuzzyGroovy.triggered.connect(self.onPlayFuzzyGroovy)
        self.ui.playButton.clicked.connect(self.onPlayAlbum)
        self.ui.stopButton.clicked.connect(self.onPauseAlbum)
        self.ui.nextButton.clicked.connect(player.mediaListPlayer.next)
        self.ui.openDirButton.clicked.connect(self.onOpenDir)
        self.ui.previousButton.clicked.connect(player.mediaListPlayer.previous)
        self.ui.searchEdit.textChanged.connect(self.onSearchChange)
        self.ui.searchEdit.returnPressed.connect(self.onSearchEnter)
        #self.ui.tableWidgetAlbums.clicked.connect(self.onAlbumChange)
        self.ui.tableWidgetAlbums.selectionModel().currentRowChanged.connect(self.onAlbumChange)
        self.ui.tableWidgetAlbums.customContextMenuRequested.connect(self.handleHeaderMenu)

        player.mpEnventManager.event_attach(vlc.EventType.MediaPlayerMediaChanged, self.onTrackChanged)


        self.ui.volumeSlider.setMaximum(100)
        self.ui.volumeSlider.setValue(player.getVolume())
        self.ui.volumeSlider.valueChanged.connect(self.setVolume)
       
        
        #Write message in status bar
        self.ui.statusBar.showMessage("PyZik")


        self.threadStreamObserver = streamObserver()
        self.threadStreamObserver.player = player
        self.threadStreamObserver.titleChanged.connect(self.setStatus)
        self.threadStreamObserver.start()


        self.loadAlbumFilesThread = loadAlbumFilesThread()
        self.loadAlbumFilesThread.setTerminationEnabled(True)
        self.loadAlbumFilesThread.imagesLoaded.connect(self.showAlbumCover)
        self.loadAlbumFilesThread.tracksLoaded.connect(self.showAlbumTracks)

        self.exploreAlbumsDirectoriesThread = exploreAlbumsDirectoriesThread()
        #self.exploreAlbumsDirectoriesThread.progressChanged.connect(self.showAlbumTracks)
        self.exploreAlbumsDirectoriesThread.exploreCompleted.connect(self.showArtists)

        self.ui.coverWidget.resizeEvent = self.resizeEvent
        
    def showEvent(self,event):
        #This function is called when the mainWindow is shown
        if self.firstShow == True:
            self.ramdomAlbum()
            self.firstShow = False

    def onPlayFuzzyGroovy(self):
        volume = player.getVolume()
        
        player.playFuzzyGroovy()
        self.setVolume(volume)
        #self.ui.volumeSlider.setValue(player.getVolume())
        #player.mpEnventManager.event_attach(vlc.EventType.MediaPlayerTitleChanged, self.nowPlayingChangedEvent)
        player.mpEnventManager.event_attach(vlc.EventType.MediaPlayerPaused, self.paused)
        player.mpEnventManager.event_attach(vlc.EventType.MediaPlayerPlaying, self.isPlaying)
        player.mpEnventManager.event_attach(vlc.EventType.MediaPlayerAudioVolume , self.setVolumeSliderFromPlayer)

        

    def ramdomAlbum(self):
        alb = mb.albumCol.getRandomAlbum()
        if(alb != None):
            print("RamdomAlb="+alb.title)
            self.showAlbum(alb)


    def setVolume(self, volume):
        player.setVolume(volume)

    def setVolumeSliderFromPlayer(self,event):
        volume = player.getVolume()
        self.ui.volumeSlider.setValue(volume)

    def setStatus(self,msg):
        #self.ui.labelArtist.setText(msg)
        self.ui.statusBar.showMessage(msg)

    def paused(self,event):
        print("Paused!")

    def isPlaying(self,event):
        print("isPlaying!")
   


    '''
    Init widgets
    '''
    def initAlbumTableWidget(self):
        self.ui.tableWidgetAlbums.setRowCount(0)
        hHeader = self.ui.tableWidgetAlbums.horizontalHeader()
        vHeader = self.ui.tableWidgetAlbums.verticalHeader()
        vHeader.hide()
        hHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        hHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        hHeader.hideSection(2)

    def initTrackTableWidget(self):
        self.ui.tableWidgetTracks.setRowCount(0)
        hHeader = self.ui.tableWidgetTracks.horizontalHeader()
        vHeader = self.ui.tableWidgetTracks.verticalHeader()
        vHeader.hide()
        hHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        hHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        hHeader.hideSection(2)
        

    '''
    Menu Actions
    '''
    def onMenuMusicDirectories(self):
        dirDiag = DialogMusicDirectoriesLoader(mb)
        dirDiag.show()
        dirDiag.exec_()
        
    def onMenuExplore(self):
        self.exploreAlbumsDirectoriesThread.musicbase = mb
        self.wProgress = progressWidget()
        self.exploreAlbumsDirectoriesThread.progressChanged.connect(self.wProgress.setValue)
        self.exploreAlbumsDirectoriesThread.directoryChanged.connect(self.wProgress.setDirectoryText)
        self.exploreAlbumsDirectoriesThread.exploreCompleted.connect(self.wProgress.close)
        self.wProgress.progressClosed.connect(self.exploreAlbumsDirectoriesThread.stop)
        self.exploreAlbumsDirectoriesThread.start()
        
    
    def onMenuDeleteDatabase(self):
        db.dropAllTables()
        mb.emptyDatas()
        self.showArtists()
        self.initAlbumTableWidget()

    def handleHeaderMenu(self, pos):
        print('column(%d)' % self.ui.tableWidgetAlbums.horizontalHeader().logicalIndexAt(pos))
        menu = QtWidgets.QMenu()
        menu.addAction('Add')
        menu.addAction('Delete')
        menu.exec(QtGui.QCursor.pos())


    '''
    Artist listView functions
    '''
    def showArtists(self):
        # Add artists in the QListView
        model = QtGui.QStandardItemModel(self.ui.listViewArtists)
        for art in mb.artistCol.artists:
            itemArt = QtGui.QStandardItem(art.name)
            itemArt.artist = art
            model.appendRow(itemArt)

        self.ui.listViewArtists.setModel(model)
        self.ui.listViewArtists.show()
        self.ui.listViewArtists.selectionModel().currentChanged.connect(self.onArtistChange)

    def setHiddenAllArtistItem(self,hide):
        #Hide all artists
        model = self.ui.listViewArtists.model()
        for i in range(model.rowCount()):
            self.ui.listViewArtists.setRowHidden(i,hide)

    def getFirstVisibleArtistItem(self):
        model = self.ui.listViewArtists.model()
        for i in range(model.rowCount()):
            if(not self.ui.listViewArtists.isRowHidden(i)):
                return model.item(i)
        
    def onArtistChange(self,item):
        #When call from listView, item is a QModelIndex
        sel = self.ui.listViewArtists.selectionModel().selectedIndexes()
        #if len(sel)==1:
        nrow = item.row()
        
        model = self.ui.listViewArtists.model()
        if self.currentArtist.artistID != model.item(nrow).artist.artistID :
            self.currentArtist = model.item(nrow).artist
            self.showAlbums(self.currentArtist)
   



    '''
    Search artist functions
    '''
    def onSearchEnter(self):
    #After typing, the user hit enter
    #to select the first artist found
        item = self.getFirstVisibleArtistItem()
        if item != None:
            selModel = self.ui.listViewArtists.selectionModel()
            selModel.reset()
            selModel.select(item.index(), QtCore.QItemSelectionModel.Select)
            self.showAlbums(item.artist)

    def onSearchChange(self,item):
        #When user write a search, shows only matching artists
        search = self.ui.searchEdit.text()

        if(len(search)==0):
            self.setHiddenAllArtistItem(False)
        else:
            self.setHiddenAllArtistItem(True)
            items = self.ui.listViewArtists.model().findItems(search,QtCore.Qt.MatchContains)
            for item in items:
                i = item.row()
                self.ui.listViewArtists.setRowHidden(i,False)



    '''
    Album tableWidget functions
    '''
    def getAlbumFromTable(self):
        #Return the selected album
        selAlbItems = self.ui.tableWidgetAlbums.selectedItems()
        for item in selAlbItems:
            r = item.row()
            albumIDSel = self.ui.tableWidgetAlbums.item(r,2).text()
            
            alb = mb.albumCol.getAlbum(albumIDSel)
            if(alb.albumID == 0): 
                print("Album is Empty. Item:"+str(item))
            return alb


    def onAlbumChange(self,item):
        if item.row() >= 0:
            print("OnAlbumChange:"+str(item.row()))
            albumIDSel = self.ui.tableWidgetAlbums.item(item.row(),2).text()
            alb = mb.albumCol.getAlbum(albumIDSel)
            if(alb.albumID != 0):
                self.showAlbum(alb)
            else:
                print("No album to show")


    def showAlbums(self,artist):
        #Add albums in the QTableView

        print("Show albums Art="+artist.name)
        self.currentAlbum = None
        self.ui.tableWidgetAlbums.setRowCount(0)
        i=0
        artist.sortAlbums()
        for alb in artist.albums:
            self.ui.tableWidgetAlbums.insertRow(i)

            titleItem = QtWidgets.QTableWidgetItem(alb.title)
            titleItem.setFlags(titleItem.flags() ^ QtCore.Qt.ItemIsEditable)
            self.ui.tableWidgetAlbums.setItem(i,0,titleItem)

            yearItem = QtWidgets.QTableWidgetItem(str(alb.year))
            yearItem.setFlags(yearItem.flags() ^ QtCore.Qt.ItemIsEditable)
            self.ui.tableWidgetAlbums.setItem(i,1,yearItem)
            
            idItem = QtWidgets.QTableWidgetItem(str(alb.albumID))
            idItem.setFlags(idItem.flags() ^ QtCore.Qt.ItemIsEditable)
            self.ui.tableWidgetAlbums.setItem(i,2,idItem)


            if(i==0):
                print("Show first album")
                self.ui.tableWidgetAlbums.selectRow(i)
                #self.onAlbumChange(self.ui.tableWidgetAlbums.item(i,0)) 
            i+=1


        #self.ui.tableWidgetAlbums.show()


    def showAlbum(self,album):
        print("showAlbum: "+album.title)
        self.currentAlbum = album
        #self.currentArtist = mb.artistCol.getArtistByID(album.artistID)
        self.setTitleLabel(self.currentArtist.name,album.title,album.year)
        
        #Start a thread to load album datas from directory
        #When updated, triggers launch showAlbumCover and showAlbumTracks
        if self.loadAlbumFilesThread.isRunning() :
            print("Stop Thread loadAlbum")
            self.loadAlbumFilesThread.stop()
            self.loadAlbumFilesThread.wait()
        
        self.loadAlbumFilesThread.album = album
        self.loadAlbumFilesThread.player = player
        self.loadAlbumFilesThread.start()


    def showAlbumTracks(self,result):        
        self.ui.tableWidgetTracks.setColumnCount(1)
        self.ui.tableWidgetTracks.setRowCount(0)
        i=0
        for track in self.currentAlbum.tracks:
            self.ui.tableWidgetTracks.insertRow(i)
            titleItem = QtWidgets.QTableWidgetItem(track.title)
            titleItem.setFlags(titleItem.flags() ^ QtCore.Qt.ItemIsEditable)
            self.ui.tableWidgetTracks.setItem(i,0,titleItem)
            i+=1

    def showAlbumCover(self,result):
        album = self.currentAlbum
        if album.cover != "":
            self.showCover(os.path.join(album.getAlbumDir(),album.cover)) 
        else:
            self.showCover("")


    '''
    Interactions with vlc module
    '''
    def playAlbum(self,alb):
        #Add tracks in playlist and start playing
        volume = player.getVolume()
        player.dropMediaList()
        player.playAlbum(alb)
        self.setVolume(volume)

        if self.playList == None:
            self.playList = playlistWidget()
            self.playList.trackChanged.connect(player.setPlaylistTrack)

        self.playList.showMediaList(player.mediaList,player)


    def onTrackChanged(self,event):
        m = player.mediaPlayer.get_media()
        if self.playList != None:
            self.playList.setCurrentTrack(m)

    def onPlayAlbum(self,item):
        print("onPlayAlbum "+self.currentAlbum.getAlbumDir())
        self.playAlbum(self.currentAlbum)

    def onPauseAlbum(self):
        player.pauseMediaList()

    def onOpenDir(self):
        open_file(self.currentAlbum.getAlbumDir())


    '''
    Miscellanious UI functions 
    '''

    def setTitleLabel(self,artName="",AlbTitle="",Year=""):
        sAlbum = AlbTitle
        sYear =str(Year)
        if(not sYear in ["0",""]): sAlbum += " ("+sYear+")"
        sTitle = '''<html><head/><body>
        <p><span style=\" font-size:14pt; font-weight:600;\">{Artist}</span></p>
        <p><span style=\" font-style:italic;\">{Album}</span></p>
        </body></html>'''
        sTitle = sTitle.format(Artist=artName,Album=sAlbum)
        
        self.ui.labelArtist.setText(sTitle)



    def showCover(self,path):
        
        if path != "":
            print("MyCover="+path)
            self.coverPixmap = QtGui.QPixmap(path)
            scaledCover = self.coverPixmap.scaled(self.ui.cover.size(),
                                                    QtCore.Qt.KeepAspectRatio,
                                                    QtCore.Qt.SmoothTransformation)
            self.ui.cover.setPixmap(scaledCover)
            self.ui.cover.show()
        else:
            self.ui.cover.setPixmap(self.defaultPixmap)
    

    def resizeEvent(self,event):
        self.resizeCover()


    def resizeCover(self):
        if (not self.coverPixmap.isNull()):
            scaledCover = self.coverPixmap.scaled(self.ui.cover.size(),
                                                    QtCore.Qt.KeepAspectRatio,
                                                    QtCore.Qt.SmoothTransformation)
            self.ui.cover.setPixmap(scaledCover)
        
    

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    mb = musicBase()

    db = database()
    
    mb.loadMusicBase()

    player = playerVLC()
    

    #Load & Set the DarkStyleSheet
    app.setStyleSheet(darkStyle.darkStyle.load_stylesheet_pyqt5())

    
    translator = QtCore.QTranslator(app)
    locale = QtCore.QLocale.system().name()
    # translator for built-in qt strings
    translator.load('pyzik_%s.qm' % locale)
    #translator.load('pyzik_es.qm')

    app.installTranslator(translator)


    window = MainWindowLoader()

    #for genre in musicGenres:
    #    print(genre+" id="+str(musicGenres.index(genre)))

    window.show()

    app.exec()
    window.threadStreamObserver.stop()
    #window.threadStreamObserver.join()
    player.release()

    sys.exit()