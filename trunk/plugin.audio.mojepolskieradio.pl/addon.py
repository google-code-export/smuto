﻿# -*- coding: utf-8 -*-
import sys
import simplejson
import urllib2

import xbmcgui
import xbmcplugin

CHANNELS_URL = 'http://moje.polskieradio.pl/api/?key=20439fdf-be66-4852-9ded-1476873cfa22&output=json'

def showChannels():
    u = urllib2.urlopen(CHANNELS_URL)
    data = u.read()
    u.close()

    channels = simplejson.loads(data[11:-1])

    for channel in channels:
        
        xbmcplugin.setContent(HANDLE, 'albums')
        
        item = xbmcgui.ListItem(channel['title'], iconImage = channel['image'], thumbnailImage = channel['image'])
        item.setProperty('IsPlayable', 'true')
        item.setProperty("IsLive", "true")
        item.setProperty('Album_Description', channel['description'])
        item.setInfo( type="Music",  infoLabels = {
                'title' : channel['title'] ,
                'artist' : channel['category'] ,
                'album' : 'moje.polskieradio.pl' ,
                'comment' : channel['description']
        })
        for i in range(len(channel["AlternateStationsStreams"])):
          if "RTSP" == channel["AlternateStationsStreams"][i]['name'] :
              rtsp = channel["AlternateStationsStreams"][i]['link'] 

        xbmcplugin.addDirectoryItem(HANDLE, str(rtsp).replace('rtsp://','rtmp://'), item)

    xbmcplugin.endOfDirectory(HANDLE)

if __name__ == '__main__':
    HANDLE = int(sys.argv[1])
    showChannels()
