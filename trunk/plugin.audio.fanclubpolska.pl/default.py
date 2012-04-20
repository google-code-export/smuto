# -*- coding: utf-8 -*-
import xbmcaddon
import simplejson
import re

from urllib2 import urlopen, Request, HTTPError, URLError

import xbmc
import xbmcgui
import xbmcplugin

__addon_name__ = 'Fanclub Polska Radio'
__id__ = 'plugin.audio.fanclubpolska.pl'
__settings__ = xbmcaddon.Addon(__id__)

HANDLE = int(sys.argv[1])
CHANNELS_URL = 'http://xbmc.org.pl/scripts/iRadio.php'

def showChannels():
    u = urlopen(CHANNELS_URL)
    data = u.read()
    u.close()
    channels = simplejson.loads(data)
    for channel in channels:
        album = channel.get('GRUPA','')
        if not album:
            album = channel.get('NAZWA','')
        bitrate = channel.get('BITRATE','0')
        if not bitrate.isdigit():
            bitrate = re.sub("\D", "", bitrate)
        item = xbmcgui.ListItem(channel['NAZWA'], iconImage = channel['URL_LOGO'], thumbnailImage = channel['URL_LOGO'])
        item.setProperty('IsPlayable', 'true')
        item.setProperty("IsLive", "true")
        item.setInfo(type="Music", infoLabels = {
                'title' : channel['NAZWA'],
                'artist' : __addon_name__  ,
                'year': int(channel.get('ROK','2012')) ,
                'size': int(bitrate) ,
                'genre': channel.get('GATUNEK','radio') ,
                'rating': channel.get('OCENA','1') ,
                'album' : album ,
                'tracknumber': int(channel['ID']),
                'comment' : channel.get('KOMENTARZ', __addon_name__)
        })
        stream_url = channel['URL_STRUMIEN']
        if channel['URL_STRUMIEN'][-3:] in ('m3u', 'pls'):
            stream_url = resolve_playlist(channel['URL_STRUMIEN'])
        item.setProperty('fanart_image', __settings__.getAddonInfo('fanart') )
        item.setProperty('Album_Description', channel.get('OPIS',''))
        xbmcplugin.setContent(HANDLE, 'albums')
        xbmcplugin.addDirectoryItem(HANDLE, stream_url, item)
        xbmcplugin.addSortMethod(HANDLE, 1, "%X")
        xbmcplugin.addSortMethod(HANDLE, 13)
        xbmcplugin.addSortMethod(HANDLE, 15)
        xbmcplugin.addSortMethod(HANDLE, 27)
        xbmcplugin.addSortMethod(HANDLE, 38, "%X")
        xbmcplugin.addSortMethod(HANDLE, 7, "%X")

    xbmcplugin.endOfDirectory(HANDLE)

def resolve_playlist(playlist_url):
    __log(u'__proba uzyskania wlasciwego adresu playlist_url=%s' % playlist_url)
    response = __urlopen(playlist_url)
    stream_url = None
    if playlist_url.endswith('m3u'):
        __log(u'__mamy plik .m3u')
        for entry in response.splitlines():
            if entry and not entry.strip().startswith('#'):
                stream_url = entry.strip()
                break
    elif playlist_url.endswith('pls'):
        __log(u'__mamy plik .pls')
        for line in response.splitlines():
            if line.strip().startswith('File1'):
                stream_url = line.split('=')[1]
                break
    if not stream_url:
        __log(u'__proba nieudana, powrot do oryginalu')
        stream_url = playlist_url
    __log('__aktualny adres strumienia to = %s' % stream_url)
    return stream_url


def __urlopen(url):
    __log('__urlopen otwiera url=%s' % url)
    req = Request(url)
    req.add_header('User-Agent', __id__)
    try:
        response = urlopen(req).read()
    except HTTPError, error:
        __log('__urlopen HTTPError: %s' % error)
        return
    except URLError, error:
        __log('__urlopen URLError: %s' % error)
        return
    __log('__urlopen koniec, wynik z %d bajtami' % len(response))
    return response

def __log(text):
    xbmc.log('%s addon: %s' % (__addon_name__, text))

if __name__ == '__main__':
    showChannels()


