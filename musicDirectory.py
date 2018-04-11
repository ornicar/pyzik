#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from albumCollection import *
from artistCollection import *

class musicDirectory:
	"""
	musicDirectory contains albums or artist's directories.
	It have a style: Various (default), Rock, Jazz...
	All his albums heritates of this style on import
	"""

	def __init__(self,sdir):
		self.db = database()
		self.dirPath = sdir
		self.musicDirectoryID = 0
		self.styleID = 0
		self.dirName = ""
		self.albums = []


	def load(self,row):
		#musicDirectoryID, dirPath, dirName, styleID
		self.musicDirectoryID = row[0]
		self.dirPath = row[1]
		self.dirName = row[2]
		self.styleID = row[3]
		

	def getDirPath(self):
		return self.dirPath
		

	def exploreAlbumsDirectory(self):
		
		dirlist = next(os.walk(self.dirPath))[1]

		for dir in dirlist:
			curAlb = album(dir)
			#curAlb.extractDataFromDirName()
			
			if curAlb.toVerify == False:
				#this album have enought datas
				newArt = artist(curAlb.artistName,0)
				artistList = self.artistCol.findArtists(newArt.name)
				
				if len(artistList)==0:
					#The artist is not in the musicBase
					curArt = self.artistCol.addArtist(newArt)
					curAlb.artistID = curArt.artistID
					curAlb.artistName = newArt.name
					curArt.albums.append(curAlb)
					print("Add artist in list"+str(curAlb.artistID))

				elif len(artistList)==1:
					#The artist is in the musicBase
					print("artist found")
					curArt = artistList[0]
					curAlb.artistID = curArt.artistID
					curAlb.artistName = curArt.name

					curArt.albums.append(curAlb)

				albumList = self.albumCol.findAlbums(curAlb.title,curAlb.artistID)
				if len(albumList)==0:
					self.albumCol.addAlbum(curAlb)
		return 



	def updateMusicDirectoryDB(self):
		if self.musicDirectoryID > 0 :
			try:
				c = self.db.connection.cursor()
				sqlInsertMusicDirectory = """	UPDATE musicDirectories SET dirPath=?, dirName=?, styleID=?
							WHERE musicDirectoryID=?;
							  """
				c.execute(sqlInsertMusicDirectory,
					(self.dirPath,
					self.dirName,
					self.styleID,
					self.musicDirectoryID))

				self.db.connection.commit()

			except sqlite3.Error as e:
				print(e)
		

