# -*- coding: utf-8 -*-
import re,string
import urllib2
import xbmcgui, xbmcplugin
import simplejson
from time import localtime, strftime

pluginUrl = sys.argv[0]
pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]

def kategorie():
    addDir('Odcinki',37,'')
    addDir('Piosenki Pana Tenorka',5810518,'')
    addDir('Dodatki',272317,'')

def get_stream_url(channel_id):
    videofileinfo = urllib2.urlopen('http://www.tvp.pl/pub/stat/videofileinfo?video_id=' + channel_id)
    json = simplejson.loads(videofileinfo.read())
    videofileinfo.close()
    return json['video_url']

def add_video_item(parent_id):
    budzik = urllib2.urlopen('http://www.api.v3.tvp.pl/shared/listing.php?dump=json&direct=false&count=150&page=1&parent_id='+parent_id+'&filter=playable=true')
    json = simplejson.loads(budzik.read())
    budzik.close()
    items = json['items']
    for item in items:
        if item['play_mode'] == 1:
            filename = str(item.get('_id',''))
            if item['samsung_enabled']:
                filename = filename+'&mime_type=video/mp4'
            print filename
            title = item.get('title','')
            date = item['release_date'].get('sec','')
            if 'image' in item:
                image = item['image'][0]['file_name']
                image = 'http://s.v3.tvp.pl/images/uid_%s_width_256_play_0_pos_0_gs_0_height_256.jpg' % (image[:-4])
            else:
                image = ''
            listitem = xbmcgui.ListItem(title, iconImage=image, thumbnailImage=image)
            listitem.setInfo('video', {'title': title, 'Date': strftime("%d.%m.%Y", localtime(date)) })
            listitem.setProperty('IsPlayable', 'true')
            xbmcplugin.addDirectoryItem(pluginHandle, pluginUrl+"?odtwarzaj="+filename, listitem, isFolder=False)

def addDir(name,parent,iconimage):
    u=pluginUrl+"?parent="+str(parent)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

if pluginQuery.startswith('?odtwarzaj='):
    channel_id = pluginQuery[11:]
    stream_url = get_stream_url(channel_id)
    xbmcplugin.setResolvedUrl(pluginHandle, True, xbmcgui.ListItem(path=stream_url))

elif pluginQuery.startswith('?parent='):
    parent_id = pluginQuery[8:]
    add_video_item(parent_id)
    xbmcplugin.addSortMethod(int(sys.argv[1]),xbmcplugin.SORT_METHOD_DATE)
 
else:
    kategorie()
xbmcplugin.endOfDirectory(pluginHandle) 
