# -*- coding: utf-8 -*-
import xbmcaddon

import sys
import simplejson
import urllib2

import xbmcgui
import xbmcplugin

__settings__ = xbmcaddon.Addon(id='plugin.audio.mojepolskieradio.pl')
__language__ = __settings__.getLocalizedString

CHANNELS_URL = 'http://moje.polskieradio.pl/api/?key=20439fdf-be66-4852-9ded-1476873cfa22&output=json'

def showChannels():
    u = urllib2.urlopen(CHANNELS_URL)
    data = u.read()
    json = simplejson.loads(data)
    u.close()
    channels = json['channel']
    for channel in channels:
        xbmcplugin.setContent(HANDLE, 'albums')
        item = xbmcgui.ListItem(channel['title'], iconImage = channel['image'], thumbnailImage = channel['image'])
        item.setProperty('IsPlayable', 'true')
        item.setProperty("IsLive", "true")
        item.setProperty('Album_Description', channel['description'].replace('\n',' '))
        item.setInfo( type="Music",  infoLabels = {
                'title' : 'PolskieRadio' ,
                'artist' : 'moje.polskieradio.pl' ,
                'year': 2012 ,
                'genre': channel['category'] ,
                'album' : channel['title'] ,
                'comment' : channel['description']
        })
        streams = channel["AlternateStationsStreams"]
        xbmc_streams = []
        for stream in streams:
            if stream['name'] == "mp3":
                link = stream['link']
                xbmc_streams.append(link)
            if  stream['name'] == "RTMP":
                link = stream['link']
                xbmc_streams.append(link)
        if __settings__.getSetting('stream') == "mp3":
            url = xbmc_streams[0]
        else:
            url = xbmc_streams[-1]
        xbmcplugin.addDirectoryItem(HANDLE, url, item)

    xbmcplugin.endOfDirectory(HANDLE)

if __name__ == '__main__':
    HANDLE = int(sys.argv[1])
    showChannels()

