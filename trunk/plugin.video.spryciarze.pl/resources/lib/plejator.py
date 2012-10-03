#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys 
import xbmc 
import xbmcgui 
import xbmcplugin 
import urllib,urllib2 
import re 
import xbmcaddon
from BeautifulSoup import BeautifulSoup, SoupStrainer

__addon__   = "plugin.video.spryciarze.pl"
__settings__ = xbmcaddon.Addon(id='plugin.video.spryciarze.pl')
IMAGES_PATH = xbmc.translatePath( os.path.join(__settings__.getAddonInfo('path'), 'resources', 'images' ) )


class Main: 
	def __init__( self ) :
 
		url = urllib.unquote_plus(sys.argv[2].split('=')[2])
		getData = urllib2.Request(url)
		response = urllib2.urlopen(getData)
		urlContent =response.read()
		response.close()
 
		numerek=re.compile('/page:(.+?)').findall(url)[0]
		nast=str(int(numerek) + 1)
		adresik=re.compile('(.+?)/page:').findall(url)[0]
		nastFin=adresik+"/page:"+nast

		next=xbmcgui.ListItem("Następna strona", iconImage=os.path.join(IMAGES_PATH,'next.png'))
		u=sys.argv[0]+"?plej&po_co="+"Następna strona"+"&url="+urllib.quote_plus(nastFin)
		xbmcplugin.addDirectoryItem(int(sys.argv[1]),u, next, isFolder=True)
 
		soupStrainer  = SoupStrainer ( "div", { "class" : "box_film" } )
		bS = BeautifulSoup( urlContent, soupStrainer )
		czystka = str(bS).replace('\t',"").replace('\r',"").replace('\n',"")
		blah=re.compile('.+?<img src="http://94.23.94.200/pic/moderacja/(.+?).jpg" .+?<a href=".+?" class="film_tytul">(.+?)</a>').findall(czystka,re.DOTALL)
		for numer,title in blah:
			gd=urllib2.Request('http://www.spryciarze.pl/player/player/xml_connect.php?code='+numer)
			response = urllib2.urlopen(gd)
			vid =response.read()
			response.close()
			vid0=re.compile('http://(.+?).flv').findall(vid)[1]
			video="http://"+vid0+".flv"
			li = xbmcgui.ListItem(title, thumbnailImage='http://94.23.94.200/pic/moderacja/'+numer+'.jpg')
			li.setInfo( type="Video", infoLabels={ "Title": title } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), video, li, isFolder=False)

		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
