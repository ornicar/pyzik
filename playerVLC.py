#!/usr/bin/env python3
# -*- coding: utf-8 -*-



##############################################
#           Play mp3 with VLC                #
##############################################

import sys
import time
import vlc
import os
from track import *
from PyQt5 import QtCore


dirtySymbols = ["@","+","*","#"]

def cleanTitle(title):
    s = title
    if s[0] in dirtySymbols:
        s = s[1:]
    if s[-1] in dirtySymbols:
        s = s[:-2]
    return s.strip()


class playerVLC:

    tracksDatas = []

    def __init__(self):

        # creating a basic vlc instance
        self.instance = vlc.Instance()
        # creating an empty vlc media player
        self.mediaPlayer = self.instance.media_player_new()
        self.mediaListPlayer = self.instance.media_list_player_new()
        self.mediaList = self.instance.media_list_new()
        self.mpEnventManager = self.mediaPlayer.event_manager()
        #self.mediaPlayer.audio_set_volume(100)
        self.radioMode = False
        self.now_playing = ""

        self.initMediaList()
           
    def release(self):
        self.mediaPlayer.release()
        self.mediaListPlayer.release()
        self.instance.release()

    def getAlbumFromMrl(self,mrl):
        trackData = [item for item in self.tracksDatas if item[0] == mrl]

        if trackData != None:
            if len(trackData) > 0:
                return trackData[0][1]
            else:
                return None
        else:
            return None

    def getTrackFromMrl(self,mrl):
        print("getTrackFromMrl="+mrl)
        trackData = [item for item in self.tracksDatas if item[0] == mrl]

        if trackData != None:
            if len(trackData) > 0:
                return trackData[0][2]
            else:
                trackData = [item for item in self.tracksDatas if item[1] == mrl]
                if len(trackData) > 0:
                    return trackData[0][2]
                else:
                    return None
        else:
            return None

    def isPlaying(self):
        return self.mediaPlayer.is_playing()

    def getCurrentIndexPlaylist(self):
        m = self.mediaPlayer.get_media()
        index = self.mediaList.index_of_item(m)
        if index == -1:
            print("count PlayList="+str(self.mediaList.count()))
            if self.mediaList.count() == 1: index = 0

        return index

    def getCurrentMrlPlaylist(self):
        m = self.mediaPlayer.get_media()
        return m.get_mrl()

    def getCurrentTrackPlaylist(self):
        mrl = self.getCurrentMrlPlaylist()
        return self.getTrackFromMrl(mrl)

    def playAlbum(self,album):
        self.radioMode = False
        
        for trk in album.tracks:
            path = os.path.join(album.getAlbumDir(),trk.getFilePathInAlbumDir())
            media = self.instance.media_new(path)
        
            self.mediaList.add_media(media)
            self.tracksDatas.append((media.get_mrl(),"",trk))

        self.playMediaList()

    def playFile(self,sfile):
        #create the media
        print(sys.version)
        if(sys.version < '3'):
            sfile = unicode(sfile)

        media = self.instance.media_new(sfile)
        # put the media in the media player
        self.mediaPlayer.set_media(media)

        # parse the metadata of the file
        media.parse()
        self.mediaPlayer.play() 

    def addFile(self,sfile):
        media = self.instance.media_new(sfile)
        media.parse()
        self.mediaList.add_media(media)

    def addFileList(self,fileList):
        for sfile in fileList:
            self.mediaList.add_media(self.instance.media_new(sfile))


    def playMediaList(self):
        self.mediaListPlayer.play()

    def stop(self):
        self.mediaPlayer.stop()


    def pauseMediaList(self):
        self.mediaListPlayer.pause()


    def initMediaList(self):
        #self.mediaList.release()
        #self.mediaListPlayer.release()
        if(self.mediaList != None):
            self.mediaList.release()
        self.mediaList = self.instance.media_list_new()
        self.mediaListPlayer.set_media_player(self.mediaPlayer)
        self.mediaListPlayer.set_media_list(self.mediaList) 

    def dropMediaList(self):
        self.mediaListPlayer.stop()
        self.mediaList.unlock()
        for i in reversed(range(0,self.mediaList.count())):
            self.mediaList.remove_index(i)


    def getVolume(self):
        """Get the volume from the player
        """
        volume = int(self.mediaPlayer.audio_get_volume())
        return volume

    def setVolume(self, Volume):
        """Set the volume
        """
        self.mediaPlayer.audio_set_volume(Volume)

    def getPosition(self):
        """Get the position in media
        """
        return self.mediaPlayer.get_position()

    def setPosition(self,pos):
        """Set the position in media
        """
        return self.mediaPlayer.set_position(pos)

    def getParsedMedia(self,sfile):
        media = self.instance.media_new(sfile)
        media.parse()
        return media

    def playFuzzyGroovy(self):
        stream = "http://listen.radionomy.com/fuzzy-and-groovy.m3u"
        self.radioMode = True
        self.dropMediaList()
        media = self.instance.media_new(stream)

        self.mediaList.add_media(media)
        self.playMediaList()
        trk = track()
        trk.radioName = "Fuzzy & Groovy Rock Radio"
        trk.radioStream = stream
        print("Fuzzy & Groovy Rock Radio isPlaying="+str(self.isPlaying()))

        #Wait until playing start
        while self.isPlaying() == 0:
            time.sleep(0.05)

        mrl = self.getCurrentMrlPlaylist()
        print("playFuzzyGroovy mrl="+mrl)
        self.tracksDatas.append((mrl,stream,trk))

    def getNowPlaying(self):
        m = self.mediaPlayer.get_media()
        if m is not None:
            now_playing = m.get_meta(12)
            if now_playing is not None:
                if self.now_playing != now_playing:
                    self.now_playing = now_playing
                    print(now_playing)
                return cleanTitle(now_playing)
            else:
                return "NO_META"
        else:
            return "NO_MEDIA"

    def getTitle(self):
        title = ""
        m = self.mediaPlayer.get_media()
        if m is not None:
            title = m.get_meta(0)
        else:
            title = "NO_TITLE"
        return title

    def getArtist(self):
        artist = ""
        m = self.mediaPlayer.get_media()
        if m is not None:
            artist = m.get_meta(1)
            if artist == None: artist = "NO_ARTIST"
        else:
            artist = "NO_ARTIST"
        return artist

    def getAlbum(self):
        album = ""
        m = self.mediaPlayer.get_media()
        if m is not None:
            album = m.get_meta(4)
        else:
            album = "NO_ALBUM"
        return album


    def getTrackNumber(self):
        number = 0
        m = self.mediaPlayer.get_media()
        if m is not None:
            number = int(m.get_meta(5))
        else:
            number = 0
        return number

    def getDate(self):
        year = ""
        m = self.mediaPlayer.get_media()
        if m is not None:
            year = m.get_meta(8)
        return year    

    def setPlaylistTrack(self,index):
        self.mediaListPlayer.play_item_at_index(index)



if __name__ == '__main__':
    player = playerVLC()
    player.initMediaList()
    player.playFuzzyGroovy()




