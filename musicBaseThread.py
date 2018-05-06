import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
from database import *
from progressWidget import *



import time


class exploreAlbumsDirectoriesThread(QThread):


    """Read datas from files in the album folder"""

    doStop = False 
    musicbase = None
    progressChanged = pyqtSignal(int, name='progressChanged')
    directoryChanged = pyqtSignal(str, name='directoryChanged')
    exploreCompleted = pyqtSignal(int, name='exploreCompleted')


    def run(self):
        self.doStop = False
        db = database()
        self.musicbase.db = db
        self.musicbase.musicDirectoryCol.db = db
       
        for mdir in self.musicbase.musicDirectoryCol.musicDirectories:
            print("explore="+mdir.dirName)
            self.directoryChanged.emit(mdir.dirName)
            mdir.db = db
            mdir.artistCol = self.musicbase.artistCol
            mdir.albumCol = self.musicbase.albumCol
            mdir.artistCol.db = db
            mdir.albumCol.db = db

            mdir.exploreDirectory(self.progressChanged)


            if self.doStop: break
        self.directoryChanged.emit("Saving datas..")
        self.musicbase.db.saveMemoryToDisc()
        self.musicbase.artistCol.sortArtists()        
        self.exploreCompleted.emit(1)
        self.quit()      
        


    def stop(self):
        self.doStop = True
        



