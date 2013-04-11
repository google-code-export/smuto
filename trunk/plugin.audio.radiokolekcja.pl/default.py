import os
import sys
import urlparse

import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs

import channels

def showChannels():
    for channel in channels.CHANNELS:
        logoImage = os.path.join(LOGO_PATH, str(channel.id) + '.png')
        if xbmcvfs.exists(logoImage):
            item = xbmcgui.ListItem(channel.name, iconImage = logoImage)
        else:
            item = xbmcgui.ListItem(channel.name, iconImage = ICON)

        item.setProperty('IsPlayable', 'true')
        item.setProperty('Fanart_Image', FANART)
        item.setInfo(type = 'music', infoLabels = {
            'title' : channel.name
        })
        xbmcplugin.addDirectoryItem(HANDLE, PATH + '?play=%d' % channel.id, item)

    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL)
    xbmcplugin.endOfDirectory(HANDLE)

def play(idx):
    channel = None
    for c in channels.CHANNELS:
        if c.id == int(idx):
            channel = c
            break

    if channel is None:
        return

    logoImage = os.path.join(LOGO_PATH, str(channel.id) + '.png')
    item = xbmcgui.ListItem(path = channel.url, thumbnailImage = logoImage)
    item.setInfo(type = 'music', infoLabels = {
        'title' : channel.name
    })
    xbmcplugin.setResolvedUrl(HANDLE, True, item)

if __name__ == '__main__':
    ADDON = xbmcaddon.Addon()
    PATH = sys.argv[0]
    HANDLE = int(sys.argv[1])
    PARAMS = urlparse.parse_qs(sys.argv[2][1:])

    LOGO_PATH = os.path.join(ADDON.getAddonInfo('path'), 'resources', 'logos')
    ICON = os.path.join(ADDON.getAddonInfo('path'), 'icon.png')
    FANART = os.path.join(ADDON.getAddonInfo('path'), 'fanart.jpg')

    if PARAMS.has_key('play'):
        play(PARAMS['play'][0])
    else:
        showChannels()