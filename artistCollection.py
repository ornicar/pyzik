#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import database
from artist import *
from database import *
from operator import itemgetter, attrgetter

def filterByName(seq, value):
	for el in seq:
		if el.name==el.formatName(value): yield el
		elif el.name.replace("AND","&")==el.formatName(value): yield el
		elif el.name==el.formatName(value).replace("AND","&"): yield el


def filterByID(seq, value):
	for el in seq:
		if el.artistID==value:
			yield el
			break




class artistCollection:
	"""
	Album's class, each album is in a directory.
	"""

	def __init__(self):
		self.artists = [] #Album Collection
		self.db = database()

		

	def addArtist(self,artist):
		#Add an artist in artists list, 


		if artist.artistID == 0:
			artist.artistID = self.insertArtistDB(artist)

		self.artists.append(artist)

		return artist


	def getArtist(self,artistName):
		newArt = artist(artistName,0)
		artistList = self.findArtists(newArt.name)

		if len(artistList)==0:
			#If the artist is not found in artistCol, we add it and return the
			curArt = self.addArtist(newArt)
			#curArt = self.artists[len(self.artists)-1] --line to delete
		elif len(artistList)==1:
			#If artists is found
			curArt = artistList[0]
		else:
			#If there is more than 1 artist, ask for the good one to user
			#For the moment, just return None
			curArt = None

		return curArt





	def findArtists(self,sname):
		artistList = []
		for art in filterByName(self.artists,sname):
			print("Found "+sname+" id="+str(art.artistID))
			artistList.append(art)
		return artistList

	def getArtistByID(self,id):
		artistList = []
		for art in filterByID(self.artists,id):
			print("Found "+str(id)+" id="+str(art.artistID))
			artistList.append(art)

		return artistList


	def printArtists(self):
		for art in self.artists:
			art.printInfos()


	def insertArtistDB(self,artist):
		sqlInsertArtist = """	INSERT INTO artists (name)
								VALUES ('{name}');
						  """.format(name=artist.name)


		try:
			c = self.db.connection.cursor()
			sqlInsertArtist = """	INSERT INTO artists (name)
								VALUES (?);
						  """
			c.execute(sqlInsertArtist,(artist.name))
			self.db.connection.commit()
			artist.artistID = c.lastrowid
		except sqlite3.Error as e:
			print(e)

		#artist.artistID = self.db.insertLine(sqlInsertArtist)

		return artist.artistID


	def loadArtists(self):
		for row_art in self.db.getSelect("SELECT artistID, name FROM artists ORDER BY name"):
			print('{0} : {1}'.format(row_art[0], row_art[1]))
			art = artist(row_art[1],row_art[0])
			self.addArtist(art)


	def artistCompare(art1,art2):
		return art1.name > art2.name

	def sortArtists(self):
		self.artists = sorted(self.artists, key=attrgetter('name'))
		#self.artists.sort(self.artistCompare)

