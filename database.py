#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3, os
from PyQt5.QtCore import pyqtSignal
from shutil import copyfile
from io import StringIO

from progressWidget import *

class database():
    '''
    Do the SQL things

    '''

    

    def __init__(self):
        self.dataPath = "./data/pyzik.db"
        self.connection = ""
        self.memoryConnection = ""

        self.createConnection()
        

    def initDataBase(self):
        self.createTableArtists()
        self.createTableAlbums()
        self.createTableMusicDirectories()
        self.createTablePlayHistoryAlbum()


    def initMemoryDB(self):

        wProgress = progressWidget()
     

        # Read database to tempfile
        print('initMemoryDB')
        tempfile = StringIO()
        i=0
        iterCount = 1000
        for line in self.connection.iterdump():
            tempfile.write('%s\n' % line)
            iProgress = round((i/iterCount)*100)
            wProgress.setValue(iProgress)
            i+=1

        self.connection.close()
        tempfile.seek(0)


        # Create a database in memory and import from tempfile
        self.memoryConnection = sqlite3.connect(":memory:")
        self.memoryConnection.cursor().executescript(tempfile.read())
        self.memoryConnection.commit()
        self.memoryConnection.row_factory = sqlite3.Row

        self.connection = self.memoryConnection

        wProgress.close()




    def saveMemoryToDisc(self):

        copyfile(self.dataPath,self.dataPath+'k')
        os.remove(self.dataPath)
        self.createConnection()
        with self.connection:
            for line in self.memoryConnection.iterdump():
                if line not in ('BEGIN;', 'COMMIT;'): # let python handle the transactions
                    self.connection.execute(line)

        self.connection.commit()


    def createConnection(self):
        """ create a database connection to the SQLite database
        specified by self.dataPath
        :return: Connection object or None
        """
        print('createConnection')
        dirPath, db_file = os.path.split(self.dataPath)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        
        try:
            self.connection = sqlite3.connect(self.dataPath)
            return self.connection
        except sqlite3.Error as e:
            print(e)
            return None

    def execSQLWithoutResult(self, sql):
        try:
            c = self.connection.cursor()
            c.execute(sql)
        except sqlite3.Error as e:
                print(e)

    def dropTable(self, table_name):
        """ drop the table called table_name
        """
        self.execSQLWithoutResult("DROP TABLE "+table_name)


    def dropAllTables(self):
        self.dropTable("artists")
        self.dropTable("albums")
        #self.dropTable("musicDirectories")

    def insertLine(self, insert_sql):
        """ insert a line from the insert_sql statement """
        try:
            c = self.connection.cursor()
            c.execute(insert_sql)
            self.connection.commit()
            return c.lastrowid
        except sqlite3.Error as e:
            print(e)
            return -1


    def createTableArtists(self):
        sqlCreateTableArtist = """  CREATE TABLE IF NOT EXISTS artists (
                                    artistID integer PRIMARY KEY,
                                    name text NOT NULL,
                                    countryID integer,
                                    categoryID integer
                                ); """
        self.execSQLWithoutResult(sqlCreateTableArtist)


    def createTableAlbums(self):
        sqlCreateTableAlbum = """ CREATE TABLE IF NOT EXISTS albums (
                                        albumID integer PRIMARY KEY,
                                        title text NOT NULL,
                                        dirName text,
                                        dirPath text,
                                        musicDirectoryID integer,
                                        artistID integer,
                                        year integer,
                                        cover text,
                                        FOREIGN KEY (artistID) REFERENCES artists(artistID),
                                        FOREIGN KEY (musicDirectoryID) REFERENCES musicDirectories(musicDirectoryID)
                                    ); """
        self.execSQLWithoutResult(sqlCreateTableAlbum)

    def createTableMusicDirectories(self):
        sqlCreateTableMusicDirectories = """ CREATE TABLE IF NOT EXISTS musicDirectories (
                                        musicDirectoryID integer PRIMARY KEY,
                                        dirPath text NOT NULL,
                                        dirName text,
                                        styleID integer
                                    ); """
        self.execSQLWithoutResult(sqlCreateTableMusicDirectories)

        if not self.columnExistsInTable("musicDirectories","dirType"):
            sqlAddcolumnDirType = """ ALTER TABLE musicDirectories ADD COLUMN dirType integer default 0 """
            self.execSQLWithoutResult(sqlAddcolumnDirType)




    def createTablePlayHistoryAlbum(self):
        sqlCreateTablePlayHistoryAlbum = """ CREATE TABLE IF NOT EXISTS playHistoryAlbum (
                                        HistoryAlbumID integer PRIMARY KEY,
                                        albumID integer,
                                        PlayDate datetime,
                                        FOREIGN KEY (albumID) REFERENCES albums(albumID)
                                    ); """
        self.execSQLWithoutResult(sqlCreateTablePlayHistoryAlbum)



    def getSelect(self,select_sql,params=None):
        c = self.connection.cursor()
        if params is None:
            c.execute(select_sql)
        else:
            c.execute(select_sql,params)
        rows = c.fetchall()
        return rows


    def columnExistsInTable(self,table,column):
        sqlExists = "PRAGMA table_info("+table+");"
        columns = self.getSelect(sqlExists)
        for col in columns:
            if column == col[1] : return True

        return False






    def insertAlbum(self,album):

        try:
            c = self.connection.cursor()
            sqlInsertAlbum = """    INSERT INTO albums (title, artistID,dirPath,year,musicDirectoryID)
                                VALUES (?,?,?,?,?);
                          """
            c.execute(sqlInsertAlbum,(album.title,album.artistID,album.dirPath,album.year,album.musicDirectoryID))
            self.connection.commit()
            album.albumID = c.lastrowid
        except sqlite3.Error as e:
            print(e)

        return album.albumID





    def insertArtist(self,artist):
        
        try:
            c = self.connection.cursor()
            sqlInsertArtist = """    INSERT INTO artists (name)
                                VALUES (?);
                          """
            c.execute(sqlInsertArtist,(artist.name,))
            self.connection.commit()
            artist.artistID = c.lastrowid
        except sqlite3.Error as e:
            print("InsertArtist error="+str(e))

        return artist.artistID
