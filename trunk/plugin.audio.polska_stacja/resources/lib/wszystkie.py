#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,re
import sys
import xbmc
import xbmcgui
import xbmcplugin
import urllib,urllib2
import xbmcaddon
from BeautifulSoup import BeautifulSoup, SoupStrainer
__addon__   = "plugin.audio.polska_stacja"
__settings__ = xbmcaddon.Addon(id='plugin.audio.polska_stacja')


class Main:
	def __init__( self ) :
		self.getNames()
	def getNames(self):
		url=urllib.unquote_plus(sys.argv[2].split('=')[0]).replace("?","")
		getData = urllib2.Request(url)
		response = urllib2.urlopen(getData)
		urlContent = response.read()
		response.close()
		sS  = SoupStrainer ( "div", { "id" : "scrollkanal" } )
		bS = BeautifulSoup( urlContent, sS )
		nl = bS.findAll ( "div", { "class" : "playerlist" } )
		czystka = str(nl).replace('\t',"").replace('\r',"").replace('\n',"")
		zzz=re.compile('<div class="playerlist" style="display:none;padding-bottom: 5px;"><a href="(.+?)" style="line-height: 20px;width:300px;display: block;float: left;" target="_blank"><img src="//cdn.polskastacja.pl/images/_winamp.png" width="16" style="vertical-align: middle; margin: 2px 5px;" border="0" alt="Radio (.+?)" />').findall(czystka)
		for url, name in zzz:
			li=xbmcgui.ListItem(name, thumbnailImage="default.png")
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)

