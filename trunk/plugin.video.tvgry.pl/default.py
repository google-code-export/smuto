# -*- coding: utf-8 -*-
import re,string
import urllib2
import xbmcgui, xbmcplugin

pluginUrl = sys.argv[0]
pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]

def get_stream_url(channel_id):
    xml = urllib2.urlopen('http://tvgry.pl/ajax_getPlaylistXML.asp?movie_ids=' + channel_id).read()
    try:
        match=re.compile('flvHD="([^"]+)').findall(xml)[0]
    except:
        match=re.compile('flvSD="([^"]+)').findall(xml)[0]
    leet = string.maketrans('abcdefghijklmnopqrstuvwxyz0123456789:-./^', 'bcdefghijklmnopqrstuvwxyza123456789:-./0_')
    return match.translate(leet)

def add_video_item():
    html = urllib2.urlopen('http://www.gry-online.pl/telewizja-dla-graczy.asp?GRU=1').read()
    for v in re.finditer('src="([^"]+)"><a href="[^0-9]+([0-9]+)"></a></div><h4>([^<]+)', html):
        img, filename, title = v.groups()
        listitem = xbmcgui.ListItem(title.decode('cp1250'), iconImage=img, thumbnailImage=img)
        listitem.setInfo('video', {'title': title.decode('cp1250') })
        listitem.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(pluginHandle, pluginUrl+"?odtwarzaj="+filename, listitem, isFolder=False)

if pluginQuery.startswith('?odtwarzaj='):
    channel_id = pluginQuery[11:]
    stream_url = get_stream_url(channel_id)
    xbmcplugin.setResolvedUrl(pluginHandle, True, xbmcgui.ListItem(path=stream_url))
else:
    add_video_item()
xbmcplugin.endOfDirectory(pluginHandle) 
