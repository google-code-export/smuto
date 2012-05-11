# -*- coding: utf-8 -*-

import xbmcgui, xbmc, xbmcaddon, xbmcplugin
import elementtree.ElementTree as ET
import urllib,urllib2,time,os

def iplaList(iplaid):
    iplaidlist = []
    elems = get_data()
    cats = elems.findall("cat")
    for cat in cats:
        val = cat.attrib
        try:
            pid = val['pid']
            if pid == str(iplaid):
                iplaidlist.append(val)
        except:
            pass
    if not iplaidlist:
        iplaVOD(iplaid)
    else:
        for item in iplaidlist:
            iplaid = item['id']
            title = item.get('title','')
            iconimage = item.get('thumbnail_big','')
            descr = item.get('descr','')
            if iplaid != '5000296':
                addDir(iplaid,title,iconimage,descr)
        xbmcplugin.addSortMethod( int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED )
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
        xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def iplaVOD(iplaid):
    darmolist = []
    elems = get_VOD_data(iplaid)
    vods = elems.find("VoDs").findall("vod")    
    for vod in vods:
        val = vod.attrib
        link = vod.findall("srcreq")[-1]
        ell = link.attrib
        drm = ell['drmtype']
        if drm == '0':
            val['url'] = ell['url']
            darmolist.append(val)
    if not darmolist:
        dialog = xbmcgui.Dialog()
        ok = dialog.ok('ipla.tv','Niestety, nie ma darmowej zawartości') 
    else:
        for item in darmolist:
            title = item.get('title','')
            if not title:
                title = item.get('descr','')
            iconimage = item.get('thumbnail_big','')
            descr = item.get('descr','')
            url = item.get('url','')
            addLink(title,url,iconimage,descr)
        xbmcplugin.addSortMethod( int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED )
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
        xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def addLink(name,url,iconimage,descr):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="video",  infoLabels = {
                'title' : name ,
                'plot': descr
        })
                #'episode': int(episode) ,
                #'season' : int(season) ,
                #'aired' : start_date
        liz.setProperty('fanart_image', __settings__.getAddonInfo('fanart') )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(iplaid,title,iconimage,descr):
    u=sys.argv[0]+"?iplaid="+str(iplaid)
    ok=True
    liz=xbmcgui.ListItem(title, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="video",  infoLabels = {
                'title' : title ,
                'plot': descr
    })
                #'episode': int(episode) ,
                #'season' : int(season) ,
                #'aired' : start_date

    liz.setProperty('fanart_image', __settings__.getAddonInfo('fanart') )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def request(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	response.close()
	return data

def download_listfile(dest):
        data = request(URL_CATEGORIES)
        f = open(dest,'w')
        f.write(unicode(data,'UTF-8').encode('UTF-8'))
        f.close()

def get_data():
	local = xbmc.translatePath(__settings__.getAddonInfo('profile'))
	if not os.path.exists(local):
		os.makedirs(local)
	local = os.path.join(local,'list.xml')
	if os.path.exists(local):
		if (time.time() - os.path.getctime(local)) > (3600*24*7):
			download_listfile(local)
	else:
		download_listfile(local)
	return ET.parse(local).getroot()

def download_VODfile(dest,iplaid):
        data = request(URL_MOVIE + str(iplaid))
        f = open(dest,'w')
        f.write(unicode(data,'UTF-8').encode('UTF-8'))
        f.close()

def get_VOD_data(iplaid):
	local = xbmc.translatePath(__settings__.getAddonInfo('profile'))
	local = os.path.join(local,str(iplaid)+'.xml')
	if os.path.exists(local):
		if (time.time() - os.path.getctime(local)) > (3600*24*7):
			download_VODfile(local,iplaid)
	else:
		download_VODfile(local,iplaid)
	return ET.parse(local).getroot()

__settings__ = xbmcaddon.Addon(id='plugin.video.ipla.pl')
URL_IPLA = 'http://getmedia.redefine.pl'
IDENTITY = 'login=5zdl1ax9&ver=313&cuid=%2D11218210'
URL_CATEGORIES = URL_IPLA + '/r/l_x_35_ipla/categories/list/?' + IDENTITY
URL_MOVIE = URL_IPLA + '/action/2.0/vod/list/?' + IDENTITY + '&category='
params=get_params()

try:
        iplaid=int(params["iplaid"])
except:
        iplaid=0
        pass

iplaList(iplaid)



