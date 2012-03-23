# -*- coding: utf-8 -*-

import urllib,urllib2,re,xbmcplugin,xbmcgui
import simplejson

import crypto.cipher.aes_cbc
import crypto.cipher.base
import binascii, time, os

try:
    from hashlib import sha1
except ImportError:
    import sha
    sha1 = sha.new


base_url = 'http://tvnplayer.pl/api/?platform=Mobile&terminal=Android&format=json'

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
            addDir(name,'getItems',type,id,'DefaultVideoPlaylists.png','')
    else:
        urlQuery = '&m=%s&type=%s&id=%s&limit=500&page=1&sort=newest' % (m, type, id)
        if season > 0:
            urlQuery = urlQuery + '&season=' + str(season)
        print base_url +urlQuery
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
                    addDir(name,'getItems',type,id,'DefaultTVShows.png',season)
        else:
            return TVNPlayerItems(json)

def TVNPlayerItems(json):
        items = json['items']
        for item in items:
            name = item.get('title','')
            type = item.get('type','')
            type_episode = item.get('type_episode','')
            id = item['id']
            if type == 'episode':
                if type_episode == 'normal' or type_episode == 'catchup':
                    tvshowtitle = item.get('title','')
                    episode = item.get('episode','')
                    sub_title = item.get('sub_title','')
                    if episode != "0":
                        name = tvshowtitle + ' - ' + sub_title + ' odc. ' + str(episode)
                    else:
                        name = tvshowtitle + ' - ' + sub_title
                    addDir(name,'getItem',type,id,'DefaultVideoCover.png','')
            else:
                thumbnail = item['thumbnail'][0]['url']
                iconimage ='http://redir.atmcdn.pl/scale/o2/tvn/web-content/m/' + thumbnail + '?type=1&quality=85&srcmode=0&srcx=49/100&srcy=1/1&srcw=27/50&srch=93/100&dstw=256&dsth=256'
                lead = item.get('lead','')
                addDir(name,'getItems',type,id,iconimage,'')

def TVNPlayerItem(type, id):
        urlQuery = '&type=%s&id=%s&sort=newest&m=getItem&deviceScreenHeight=1080&deviceScreenWidth=1920' % (type, id)
        print base_url + urlQuery
        getItems = urllib2.urlopen(base_url + urlQuery)
        json = simplejson.loads(getItems.read())
        getItems.close()
        serie_title = json['item'].get('serie_title','')
        title = json['item'].get('title', '')
        lead = json['item'].get('lead','')
        episode = json['item'].get('episode','')
        season = json['item'].get('season','')
        start_date = json['item'].get('start_date','')
        video_content = json['item']['videos']['main']['video_content']
        videoUrls={}
        for video in video_content:
            qualityName = video['profile_name']
            videoUrl = video['url']
            rank = 'z'
            if qualityName == 'Bardzo wysoka':
                rank = 'a'
            elif qualityName == 'Wysoka':
                rank = 'b'
            elif qualityName == 'Standard':
                rank = 'c'
            elif qualityName == 'Niska':
                rank = 'd'
            if rank != 'z':
                videoUrls[rank] = videoUrl
            else:
                print qualityName
        rankSorted =sorted(videoUrls)
        if len(rankSorted) > 0:
            url = videoUrls.get(rankSorted[0])
            url = generateToken(url)
        else:
            url = ''
        thumbnail = json['item']['thumbnail'][0]['url']
        if not title:
            if episode != "0":
                title = serie_title + ' - odc. ' + str(episode)
            else:
                title = serie_title
        ok=True
        xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
        liz=xbmcgui.ListItem(title, iconImage="DefaultVideo.png", thumbnailImage='http://redir.atmcdn.pl/scale/o2/tvn/web-content/m/' + thumbnail + '?quality=85&dstw=640&dsth=360&type=1')
        liz.setProperty('IsPlayable', 'true')
        liz.setProperty("IsLive", "true")
        liz.setInfo( type="video",  infoLabels = {
                'tvshowtitle' : serie_title ,
                'title' : title ,
                'plot': htmlToText(lead) ,
                'episode': int(episode) ,
                'season' : int(season) ,
                'aired' : start_date
        })
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def htmlToText(html):
    html = re.sub('<.*?>','',html)
    return html .replace("&lt;", "<")\
                .replace("&gt;", ">")\
                .replace("&amp;", "&")\
                .replace("&quot;",'"')\
                .replace("&apos;","'")

def SetTVNPlayer():
        return TVNPlayerAPI(platform='Mobile',terminal='Android',format='json')

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

def generateToken(url):
        url = url.replace('http://redir.atmcdn.pl/http/','')
        SecretKey = 'AB9843DSAIUDHW87Y3874Q903409QEWA'
        iv = 'ab5ef983454a21bd'
        KeyStr = '0f12f35aa0c542e45926c43a39ee2a7b38ec2f26975c00a30e1292f7e137e120e5ae9d1cfe10dd682834e3754efc1733'
        salt = sha1()
        salt.update(os.urandom(16))
        salt = salt.hexdigest()[:32]
        tvncrypt = crypto.cipher.aes_cbc.AES_CBC(SecretKey, padding=crypto.cipher.base.noPadding(), keySize=32)
        key = tvncrypt.decrypt(binascii.unhexlify(KeyStr), iv=iv)[:32]
        expire = 3600000L + long(time.time()*1000) - 946684800000L
        unencryptedToken = "name=%s&expire=%s\0" % (url, expire)
        pkcs5_pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        pkcs5_unpad = lambda s : s[0:-ord(s[-1])]
        unencryptedToken = pkcs5_pad(unencryptedToken)
        tvncrypt = crypto.cipher.aes_cbc.AES_CBC(binascii.unhexlify(key), padding=crypto.cipher.base.noPadding(), keySize=16)
        encryptedToken = tvncrypt.encrypt(unencryptedToken, iv=binascii.unhexlify(salt))
        encryptedTokenHEX = binascii.hexlify(encryptedToken).upper()
        return "http://redir.atmcdn.pl/http/%s?salt=%s&token=%s" % (url, salt, encryptedTokenHEX)  

def addDir(name,m,type,id,iconimage,season):
        u=sys.argv[0]+"?m="+urllib.quote_plus(m)+"&type="+urllib.quote_plus(type)+"&id="+str(id)+"&season="+str(season)+"&platform=Mobile&terminal=Android"
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
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

xbmcplugin.endOfDirectory(int(sys.argv[1]))
