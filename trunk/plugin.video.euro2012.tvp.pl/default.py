# -*- coding: utf-8 -*-
import xbmcaddon
import re,string
import urllib2
import xbmcgui, xbmcplugin
import simplejson
from time import localtime, strftime, time

__addon_name__ = 'Euro2012.tvp.pl'
__id__ = 'plugin.video.euro2012.tvp.pl'
__settings__ = xbmcaddon.Addon(__id__)

pluginUrl = sys.argv[0]
pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]
listing_url = 'http://www.api.v3.tvp.pl/shared/listing.php?dump=json'
urlImage = 'http://s.v3.tvp.pl/images/%s/%s/%s/uid_%s_width_%d_gs_0.jpg'

def tvpAPI(parent_id):
    url = listing_url + '&direct=true&count=150&parent_id=%s'% (parent_id)
    response = urllib2.urlopen(url)
    json = simplejson.loads(response.read())
    response.close()
    items = json['items']
    if not items:
        print 'pusta'
        parentlist = []
        parent_id = json['query']['parent_node_id']
        url = listing_url + '&filter=playable=true&direct=false&count=500&page=1&parent_id=%s'% (parent_id)
        response = urllib2.urlopen(url)
        json = simplejson.loads(response.read())
        response.close()
        podkatalogi = json['items']
        if not podkatalogi:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('tvp','Niestety, ta lista też pusta')
        else:
            title = json['items'][0].get('website_title','')
            for item in podkatalogi:
                parent_id = item.get('parent_node_id','')
                parentlist.append(parent_id)
            parentlist = set(parentlist)
            ct=1;
            for item in parentlist:
                addDir(title+' '+str(ct),item,__settings__.getAddonInfo('icon'))
                ct+=1
            xbmcplugin.endOfDirectory(pluginHandle)
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
        ok = dialog.ok('tvp','Niestety, pusta lista')
    else:
        for item in darmowe:
            if 'samsung_enabled' in item:
                if item['release_date'].get('sec','') < time() and item['play_mode'] != 0:
                    filename = str(item.get('_id',''))
                    if item['samsung_enabled']:
                        filename = filename+'&mime_type=video/mp4'
                    title = item.get('title','')
                    TVShowTitle =  item.get('website_title','')
                    if 'description_root' in item:
                        desc =  item.get('description_root','')
                    else:
                        desc =  item.get('lead_root','')
                    aired =  item.get('publication_start_dt','')
                    date = item['release_date'].get('sec',time())
                    if str(date).startswith('-'):
                        date= time()
                    iconUrl = getImageUrl(item)
                    listitem = xbmcgui.ListItem(title, iconImage=iconUrl, thumbnailImage=iconUrl)
                    listitem.setInfo('video', {'title': title,'tvshowtitle': TVShowTitle,'plot': desc,'aired': aired, 'Date': strftime("%d.%m.%Y", localtime(date)) })
                    listitem.setProperty('fanart_image', __settings__.getAddonInfo('fanart') )
                    listitem.setProperty('IsPlayable', 'true')
                    xbmcplugin.setContent(pluginHandle, 'episodes')
                    xbmcplugin.addDirectoryItem(pluginHandle, pluginUrl+"?odtwarzaj="+filename, listitem, isFolder=False)
                    xbmcplugin.addSortMethod(pluginHandle,xbmcplugin.SORT_METHOD_DATE)
            else:
                title = item.get('title','')
                filename = str(item.get('asset_id',''))
                addDir(title,filename,__settings__.getAddonInfo('icon'))
        xbmcplugin.endOfDirectory(pluginHandle) 


def getImageUrl(item):
        iconUrl = ""

        if 'image' in item:
            iconFile = item['image'][0]['file_name'].encode('utf-8')
            iconWidth = item['image'][0]['width']
            if iconWidth > 0:
                iconUrl = urlImage %(iconFile[0],iconFile[1],iconFile[2],iconFile[:-4],iconWidth)

        elif iconUrl == '' and 'image_4x3' in item:
            iconFile = item['image_4x3'][0]['file_name'].encode('utf-8')
            iconWidth = item['image_4x3'][0]['width']
            if iconWidth > 0:
                iconUrl = urlImage %(iconFile[0],iconFile[1],iconFile[2],iconFile[:-4],iconWidth)

        elif iconUrl == '' and  'image_ns644' in item:
            iconFile = item['image_ns644'][0]['file_name'].encode('utf-8')
            iconWidth = item['image_ns644'][0]['width']
            if iconWidth > 0:
                iconUrl = urlImage %(iconFile[0],iconFile[1],iconFile[2],iconFile[:-4],iconWidth)

        elif iconUrl == '' and  'image_ns954' in item:
            iconFile = item['image_ns954'][0]['file_name'].encode('utf-8')
            iconWidth = item['image_ns954'][0]['width']
            if iconWidth > 0:
                iconUrl = urlImage %(iconFile[0],iconFile[1],iconFile[2],iconFile[:-4],iconWidth)

        else:
            iconUrl = __settings__.getAddonInfo('icon')

        print iconUrl
        return iconUrl

def get_stream_url(channel_id):
    print 'http://www.tvp.pl/pub/stat/videofileinfo?video_id=' + channel_id 
    videofileinfo = urllib2.urlopen('http://www.tvp.pl/pub/stat/videofileinfo?video_id=' + channel_id)
    json = simplejson.loads(videofileinfo.read())
    videofileinfo.close()
    if json['video_url'].endswith('manifest'):
        if json['file_name'].endswith('Ch0015'):
            return 'http://195.245.213.204/Ch0006'
        else:
            print json['file_name']
    else:
        return json['video_url']


def addDir(name,parent,iconimage):
    u=pluginUrl+"?parent="+str(parent)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty('fanart_image', __settings__.getAddonInfo('fanart') )
    ok=xbmcplugin.addDirectoryItem(pluginHandle,url=u,listitem=liz,isFolder=True)
    return ok

if pluginQuery.startswith('?odtwarzaj='):
    channel_id = pluginQuery[11:]
    stream_url = get_stream_url(channel_id)
    xbmcplugin.setResolvedUrl(pluginHandle, True, xbmcgui.ListItem(path=stream_url))

else:
    parent_id = pluginQuery[8:]
    if not parent_id:
        addDir('transmisje','3116100',__settings__.getAddonInfo('icon'))
        results = []
        for start in (5770492,7020280,7196752):
            url = listing_url + '&direct=true&count=150&parent_id=%s'% (start)
            response = urllib2.urlopen(url)
            json = simplejson.loads(response.read())
            response.close()
            results += json['items']
        for item in results:
            title = item.get('title','')
            filename = str(item.get('asset_id',''))
            if filename != '7010741' and filename != '7375438':
                addDir(title,filename,__settings__.getAddonInfo('icon'))
        xbmcplugin.endOfDirectory(pluginHandle) 
    else:
        print 'ParentID:'+parent_id 
        tvpAPI(parent_id)

