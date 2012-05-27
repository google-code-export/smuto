# -*- coding: utf-8 -*-
import re,string
import urllib2
import xbmcgui, xbmcplugin
import simplejson
from time import localtime, strftime

pluginUrl = sys.argv[0]
pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]
listing_url = 'http://www.api.v3.tvp.pl/shared/listing.php?dump=json'

def tvpAPI(parent_id):
    url = listing_url + '&direct=true&count=101&parent_id=%s'% (parent_id)
    response = urllib2.urlopen(url)
    json = simplejson.loads(response.read())
    response.close()
    items = json['items']
#   if not items:
#        parent_id = json['query']['parent_node_id']
#        url = listing_url + '&filter=playable=true&direct=false&count=300&page=1&parent_id=%s'% (parent_id)
#        response = urllib2.urlopen(url)
#        json = simplejson.loads(response.read())
#        response.close()
#        items = json['items']    
    lista_pozycji = []
    for item in items:
        title = item.get('title','')
        lista_pozycji.append(title)
    if 'wideo' in lista_pozycji:
        for item in items:
            if 'wideo' in item.get('title',''):
                filename = str(item.get('_id',''))
                return tvpAPI(filename)
    else:
        return listingTVP(json)
        

def listingTVP(json):
    categories = json['items']
    darmowe=[]
    for item in categories:
        if 'samsung_enabled' in item:
            if not item['payable']:
                darmowe.append(item)
        else:
            darmowe.append(item)

    if not darmowe:
        dialog = xbmcgui.Dialog()
        ok = dialog.ok('tvp','Niestety, nie ma darmowej zawartości')
        return
    else:
        for item in darmowe:
            if 'samsung_enabled' in item:
                filename = str(item.get('_id',''))
                if item['samsung_enabled']:
                    filename = filename+'&mime_type=video/mp4'
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
            else:
                title = item.get('title','')
                filename = str(item.get('_id',''))
                if filename != '1597829':
                    addDir(title,filename,'')
 
def get_stream_url(channel_id):
    videofileinfo = urllib2.urlopen('http://www.tvp.pl/pub/stat/videofileinfo?video_id=' + channel_id)
    json = simplejson.loads(videofileinfo.read())
    videofileinfo.close()
    return json['video_url']


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

else:
    parent_id = pluginQuery[8:]
    if not parent_id:
        parent_id = '1785454'
    tvpAPI(parent_id)
    xbmcplugin.addSortMethod(int(sys.argv[1]),xbmcplugin.SORT_METHOD_DATE)
xbmcplugin.endOfDirectory(pluginHandle) 
