# -*- coding: utf-8 -*-
import xbmcaddon

import urllib2, simplejson
import xbmc, xbmcgui, xbmcplugin


class multiImagesSession:

    def addLink(self,name,url):
        liz=xbmcgui.ListItem(name, iconImage="DefaultImage.png")
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)

    def LIBRARY_FANARTS(self):
        retval = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "AudioLibrary.GetArtists", "params": {"properties": ["fanart"] }, "id": 1}')
        result = simplejson.loads(retval)
        images = result['result']['artists']
        for img in images:
            title = img.get('label','')
            if not self.addLink(title,img.get('fanart','')): break
        return True

    def SEARCH_FANARTS(self,query):
        results = []
        url = 'http://pipes.yahoo.com/pipes/pipe.run?_id=65dbeb994f0d10b36ed8a8f0fcc83a8d&keywords='+query.replace(' ','+')+'&_render=json'
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        data=response.read()
        response.close()
        result = simplejson.loads(data)
        images = result['value']['items']
        for img in images:
            title = img.get('title','')
            if not self.addLink(title,img.get('link','')): break
        return True


## XBMC Plugin stuff starts here --------------------------------------------------------            
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
    

### Do plugin stuff --------------------------------------------------------------------------
def doPlugin():
    params=get_params()

    mode=None
    name=None
    if xbmc.Player().isPlayingAudio()==False:
        url=None

    else:
        artist=xbmc.Player().getMusicInfoTag().getArtist()
        url=artist.replace('&','')
    try:
            url=urllib.unquote_plus(params["url"])
    except:
            pass
    try:
            name=urllib.unquote_plus(params["name"])
    except:
            pass
    try:
            mode=int(params["mode"])
    except:
            pass

    print "Mode: "+str(mode)
    print "URL: "+str(url)
    print "Name: "+str(name)


    update_dir = True
    success = True
    cache = True

    mis = multiImagesSession()
    
#    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TRACKNUM)
    
    if mode==None and url==None or len(url)<1:
        mis.LIBRARY_FANARTS()
    else:
        mis.SEARCH_FANARTS(query=url)

    xbmcplugin.endOfDirectory(int(sys.argv[1]),succeeded=success,updateListing=update_dir,cacheToDisc=cache)

doPlugin()