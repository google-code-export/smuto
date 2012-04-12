# -*- coding: utf-8 -*-
import xbmcaddon

import urllib,urllib2,re,string,xbmc,xbmcgui,xbmcplugin
import simplejson
from BeautifulSoup import BeautifulSoup as BS

MAIN_URL = 'http://www.lechpoznan.tv'

def CATEGORIES():
        addDir('News','/filmy/News',1,1,'','')
        addDir('Mecze','/filmy/Mecze',1,1,'','')
        addDir('Programy','/filmy/Programy',1,1,'','')
        addDir('Szukaj','/Catalog/Search',1,1,'','')

def INDEX(url,page,query):
        if 'Search' in url:
            if not query:
                query = getTerms()
                if not query:
                    return -1           
            base_url = MAIN_URL+url+'?SearchQuery='+query+'&page='+page
        else:
            base_url = MAIN_URL+url+'?page='+page

        req = urllib2.Request(base_url)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        try:
                lastPage = re.compile('([0-9]*)" class="lastPage"').findall(link)[0];
        except:
                lastPage = "1";
                pass
        link = string.split(link,'class="movieListM"')
        if len(link)>=2:
            link = string.split(link[1],'class="pagerBox"')
            link = string.split(link[0],'class="movieBox"')
            for movie in link[1:]:
                name = re.compile('titleBox">([^<]+)').findall(movie)[0]
                match=re.compile('href="([^"]+)').findall(movie)[0]
                video_url = sys.argv[0]+"?mode=2&url="+match
                thumb = re.compile('src="([^"]+)').findall(movie)[0]
                miesiac = re.compile('left">([^<]+)').findall(movie)[0]
                date = miesiac.replace(" stycznia ", ".01.")\
                            .replace(" lutego ", ".02.")\
                            .replace(" marca ", ".03.")\
                            .replace(" kwietnia ", ".04.")\
                            .replace(" maja ", ".05.")\
                            .replace(" czerwca ", ".06.")\
                            .replace(" lipca ", ".07.")\
                            .replace(" sierpnia ", ".08.")\
                            .replace(" września ", ".09.")\
                            .replace(" października ", ".10.")\
                            .replace(" listopada ", ".11.")\
                            .replace(" grudnia ", ".12.")
                addLink(name,video_url,thumb,date,miesiac,page)
        else:
            return -1              
        ipage = int(page);
        if ipage > 1:
                addDir(__language__(30001),url,1,str(ipage-1),'',query)
        if ipage < int(lastPage):
                addDir(__language__(30000),url,1,str(ipage+1),'',query)
        xbmcplugin.addSortMethod(int(sys.argv[1]),xbmcplugin.SORT_METHOD_DATE)

def getTerms():
        keyboard = xbmc.Keyboard('','LechTV Online')
        keyboard.doModal()
        if (keyboard.isConfirmed()):
            return keyboard.getText()
        else:
            return ''

def RESOLVE(url):
        req2 = urllib2.Request(MAIN_URL+url)
        response = urllib2.urlopen(req2)
        link = response.read()
        response.close()
        match=re.compile('var content = ([^;]+)').findall(link)[0]
        json = simplejson.loads(match)
        try:
                stream_url = json['formats'][0]['url'];
        except:
                stream_url = "";
                pass
        if stream_url:
            xbmcplugin.setResolvedUrl(pluginHandle, True,
                                  xbmcgui.ListItem(path=stream_url))
        else:
            xbmcplugin.setResolvedUrl(pluginHandle, False,
                                  xbmcgui.ListItem())
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('','LechTV Online') 


def addLink(name,url,iconimage,date,miesiac,page):
        ok=True
        name=str(BS(name,convertEntities=BS.HTML_ENTITIES,fromEncoding='utf-8'))
        xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="video",  infoLabels = {
                "Title": name ,
                "aired": miesiac ,
                "episode": int(page) ,
                "tvshowtitle": "LechTV Online" ,
                "plot": __language__(30002) ,
                "Date": date
        })
        liz.setProperty('fanart_image', __settings__.getAddonInfo('fanart') )
        liz.setProperty("IsPlayable","true");
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
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

def addDir(name,url,mode,page,iconimage,query):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&page="+str(page)+"&query="+urllib.quote_plus(query)
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image', __settings__.getAddonInfo('fanart') )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

__settings__ = xbmcaddon.Addon(id='plugin.video.lechtv.pl')
__language__ = __settings__.getLocalizedString
pluginUrl = sys.argv[0]
pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]
params=get_params()
url=None
mode=None
query=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        query=urllib.unquote_plus(params["query"])
except:
        pass
try:
        page = params["page"]
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass


if mode==None or url==None or len(url)<1:
        CATEGORIES()
       
elif mode==1:
        INDEX(url,page,query)

        
elif mode==2:
        RESOLVE(url)


xbmcplugin.endOfDirectory(pluginHandle)
