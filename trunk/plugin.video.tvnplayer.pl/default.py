# -*- coding: utf-8 -*-

import urllib,urllib2,re,xbmcplugin,xbmcgui
import simplejson, socket


pluginUrl = sys.argv[0]
pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]
base_url = 'http://tvnplayer.pl/api/?platform=ConnectedTV&terminal=Samsung&format=json'
scale_url = 'http://redir.atmcdn.pl/scale/o2/tvn/web-content/m/'

socket.setdefaulttimeout(10)

def TVNPlayerAPI(m,type,id,season):
    if m == 'mainInfo':
        url = base_url + '&m=%s'% (m)
        response = urllib2.urlopen(url)
        json = simplejson.loads(response.read())
        response.close()
        categories = json['categories']
        for item in categories:
            name = item.get('name','')
            type = item.get('type','')
            id = item['id']
            if type != 'titles_of_day':
                addDir(name,'getItems',type,id,'DefaultVideoPlaylists.png','','')
    else:
        urlQuery = '&m=%s&type=%s&id=%s&limit=500&page=1&sort=newest' % (m, type, id)
        if season > 0:
            urlQuery = urlQuery + '&season=' + str(season)
        response = urllib2.urlopen(base_url + urlQuery)
        json = simplejson.loads(response.read())
        response.close()
        if type == "series":
            if json['items'][0]['season'] == str(season):
                return TVNPlayerItems(json)
            else:
                seasons = json['seasons']
                for item in seasons:
                    name = item.get('name','')
                    season = item.get('id','')
                    xbmcplugin.addSortMethod(pluginHandle, xbmcplugin.SORT_METHOD_LABEL)
                    addDir(name,'getItems',type,id,'DefaultTVShows.png','',season)
                if not seasons:
                    return TVNPlayerItems(json)
        else:
            return TVNPlayerItems(json)

def TVNPlayerItems(json):
        items = json['items']
        for item in items:
            name = item.get('title','')
            type = item.get('type','')
            type_episode = item.get('type_episode','')
            id = item['id']
            thumbnail = item['thumbnail'][0]['url']
            gets = {'type': 1,
                    'quality': 95,
                    'srcmode': 0,
                    'srcx': item['thumbnail'][0]['srcx'],
                    'srcy': item['thumbnail'][0]['srcy'],
                    'srcw': item['thumbnail'][0]['srcw'],
                    'srch': item['thumbnail'][0]['srch'],
                    'dstw': 256,
                    'dsth': 292}
            if type == 'episode':
                if type_episode == 'normal' or type_episode == 'catchup':
                    tvshowtitle = item.get('title','')
                    episode = item.get('episode','')
                    sub_title = item.get('sub_title','')
                    lead = item.get('lead','')
                    season = item.get('season','')
                    start_date = item.get('start_date','')
                    url = pluginUrl+'?m=getItem&id='+str(id)+'&type='+type
                    name = tvshowtitle + ' - ' + sub_title
                    if not sub_title or tvshowtitle == sub_title:
                        name = tvshowtitle
                    if type_episode == 'catchup':
                        name = name + ', sezon ' + str(season)+', odcinek '+ str(episode)
                        
                    addLink(name,url,thumbnail,gets,tvshowtitle,lead,episode,season,start_date)
            else:
                addDir(name,'getItems',type,id,thumbnail,gets,'')

def TVNPlayerItem(type, id):
        urlQuery = '&type=%s&id=%s&sort=newest&m=getItem&deviceScreenHeight=1080&deviceScreenWidth=1920' % (type, id)
        getItem = urllib2.urlopen(base_url + urlQuery)
        json = simplejson.loads(getItem.read())
        getItem.close()
        video_content = json['item']['videos']['main']['video_content']
        profile_name_list = []
        for item in video_content:
            profile_name = item['profile_name']
            profile_name_list.append(profile_name)
        select = xbmcgui.Dialog().select('Wybierz jakość', profile_name_list)
        stream_url = json['item']['videos']['main']['video_content'][select]['url']
        xbmcplugin.setResolvedUrl(pluginHandle, True, xbmcgui.ListItem(path=stream_url))

def htmlToText(html):
    html = re.sub('<.*?>','',html)
    return html .replace("&lt;", "<")\
                .replace("&gt;", ">")\
                .replace("&amp;", "&")\
                .replace("&quot;",'"')\
                .replace("&apos;","'")

def SetTVNPlayer():
        return TVNPlayerAPI(platform='Mobile',terminal='Sony',format='json')

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


def addDir(name,m,type,id,thumbnail,gets,season):
        u=sys.argv[0]+"?m="+urllib.quote_plus(m)+"&type="+urllib.quote_plus(type)+"&id="+str(id)+"&season="+str(season)
        if not gets:
            thumbnailimage=''
        else:
            thumbnailimage='%s%s?%s' % (scale_url, thumbnail, urllib.urlencode(gets))
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=urllib.unquote(thumbnailimage))
        liz.setInfo( type="video",  infoLabels = {'title' : name })
        ok=xbmcplugin.addDirectoryItem(handle=pluginHandle,url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name,url,thumbnail,gets,serie_title,lead,episode,season,start_date):
        ok=True
        if not gets:
            thumbnailimage=''
        else:
            thumbnailimage='%s%s?%s' % (scale_url, thumbnail, urllib.urlencode(gets))
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=urllib.unquote(thumbnailimage))
        liz.setInfo( type="video",  infoLabels = {
                'tvshowtitle' : serie_title ,
                'title' : name ,
                'plot': htmlToText(lead) ,
                'episode': int(episode) ,
                'season' : int(season) ,
                'aired' : start_date
        })
        liz.setProperty("IsPlayable","true");
        liz.setProperty('Fanart_Image', 'http://dcs-46-28-242-53.atmcdn.pl/dcs/o2/tvn/web-content/m/orig/' + thumbnail)
        ok=xbmcplugin.addDirectoryItem(handle=pluginHandle,url=url,listitem=liz,isFolder=False)
        return ok

params=get_params()

type=None
id=None

limit=None
page=None

try:
        m=urllib.unquote_plus(params["m"])
except:
        m="mainInfo"
        pass
try:
        type=urllib.unquote_plus(params["type"])
except:
        pass
try:
        id=int(params["id"])
except:
        pass
try:
        season=int(params["season"])
except:
        season="0"
        pass

print "Tryb: "+str(m)
print "Typ: "+str(type)
print "ID: "+str(id)
print "Sezon: "+str(season)

if m == "mainInfo":
        TVNPlayerAPI(m,type,id,season)
       
elif m == "getItems":
        TVNPlayerAPI(m,type,id,season)
        
elif m == "getItem":
        TVNPlayerItem(type,id)

if type == "series":
        xbmcplugin.setContent(pluginHandle, 'episodes')
        xbmcplugin.addSortMethod(pluginHandle, xbmcplugin.SORT_METHOD_EPISODE)
elif type == "catalog":
        xbmcplugin.addSortMethod( pluginHandle, xbmcplugin.SORT_METHOD_UNSORTED )
        xbmcplugin.addSortMethod(pluginHandle, xbmcplugin.SORT_METHOD_LABEL)
        if id == 3:
            xbmcplugin.setContent(pluginHandle, 'movies')
xbmcplugin.endOfDirectory(pluginHandle)
