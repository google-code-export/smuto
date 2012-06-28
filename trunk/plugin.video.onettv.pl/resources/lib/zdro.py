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
			("Zdrowie dla każdego",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=34&tags=%28Zdrowie_dla_ka%C5%BCdego%29&rss=1'),
			("Kobiece choroby",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=34&tags=%28Kobiece_choroby%29&rss=1'),
			("Choroby dziecięce",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=34&tags=%28Choroby_dzieci%C4%99ce%29&rss=1'),
			("Problemy seniorów",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=34&tags=%28Problemy_senior%C3%B3w%29&rss=1'),
			(alL,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=34&rss=1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?RSS&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
