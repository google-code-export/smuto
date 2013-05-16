# -*- coding: utf-8 -*-
import sys
import simplejson
import urllib2

import xbmcgui
import xbmcplugin

CHANNELS_URL = 'http://pipes.yahoo.com/pipes/pipe.run?_id=658c65eac05da916cff8929d5f9d8703&_render=json'

def showPictures():
    u = urllib2.urlopen(CHANNELS_URL)
    data = u.read()
    u.close()

    result = simplejson.loads(data)
    pictures = result['value']['items']

    for picture in pictures:
        
        item = xbmcgui.ListItem(picture['description'], iconImage = "DefaultPicture.png")

        xbmcplugin.addDirectoryItem(HANDLE, picture['media:group']['media:content']['url'], item)

    xbmcplugin.endOfDirectory(HANDLE)

if __name__ == '__main__':
    HANDLE = int(sys.argv[1])
    showPictures()

