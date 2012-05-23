# -*- coding: utf-8 -*-
import re,string
import urllib2
import xbmcgui, xbmcplugin
import simplejson
from time import localtime, strftime

pluginUrl = sys.argv[0]
pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]

def get_stream_url(channel_id):
    videofileinfo = urllib2.urlopen('http://www.tvp.pl/pub/stat/videofileinfo?video_id=' + channel_id)
    json = simplejson.loads(videofileinfo.read())
    videofileinfo.close()
    return json['video_url']

def add_video_item():
    budzik = urllib2.urlopen('http://www.api.v3.tvp.pl/shared/listing.php?parent_id=37&direct=false&count=150&page=1&filter=payable=false&dump=json')
    json = simplejson.loads(budzik.read())
    budzik.close()
    items = json['items']
    for item in items:
        if item['play_mode'] == 1:
            filename = str(item.get('_id',''))
            title = item.get('title','')
            date = item['release_date'].get('sec','')
            print date
            if 'image' in item:
                image = item['image'][0]['file_name']
                image = 'http://s.v3.tvp.pl/images/uid_%s_width_256_play_0_pos_0_gs_0_height_256.jpg' % (image[:-4])
            else:
                image = ''
            listitem = xbmcgui.ListItem(title, iconImage=image, thumbnailImage=image)
            listitem.setInfo('video', {'title': title, 'Date': strftime("%d.%m.%Y", localtime(date)) })
            listitem.setProperty('IsPlayable', 'true')
            xbmcplugin.addDirectoryItem(pluginHandle, pluginUrl+"?odtwarzaj="+filename, listitem, isFolder=False)

if pluginQuery.startswith('?odtwarzaj='):
    channel_id = pluginQuery[11:]
    stream_url = get_stream_url(channel_id)
    xbmcplugin.setResolvedUrl(pluginHandle, True, xbmcgui.ListItem(path=stream_url))
else:
    add_video_item()
    xbmcplugin.addSortMethod(int(sys.argv[1]),xbmcplugin.SORT_METHOD_DATE)
    xbmcplugin.endOfDirectory(pluginHandle) 
