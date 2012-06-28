#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import urllib
import xbmcaddon

__addon__   = "plugin.video.onettv.pl"
__settings__ = xbmcaddon.Addon(id='plugin.video.onettv.pl')
names = __settings__.getLocalizedString

alL = (names (33333))

#HOME_DIR = os.getcwd()
#names = xbmc.Language( HOME_DIR ).getLocalizedString

class Main:
	#
	# Init
	#
	def __init__( self ) :

		self.getNames()

	def getNames(self):
		gl=[
			("Komórki",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=31&tags=%28Kom%C3%B3rki%29&rss=1'),
			("Laptopy",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=31&tags=%28Laptopy%29&rss=1'),
			("Foto",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=31&tags=%28Foto%29&rss=1'),
			("RTV",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=31&tags=%28RTV%29&rss=1'),
			("Internet i programy",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=31&tags=%28Internet_i_programy%29&rss=1'),
			("GPS",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=31&tags=%28GPS%29&rss=1'),
			(alL,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=31&rss=1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?RSS&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
