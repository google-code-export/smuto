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
			("Design",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=33&tags=%28Design%29&rss=1'),
			("Architektura",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=33&tags=%28Architektura%29&rss=1'),
			("Porady",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=33&tags=%28Porady%29&rss=1'),
			("Metamorfozy",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=33&tags=%28Metamorfozy%29&rss=1'),
			("Wnętrzarskie inspiracje",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=33&tags=%28Wn%C4%99trzarskie_inspiracje%29&rss=1'),
			("Gwiazdy",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=33&tags=%28Gwiazdy%29&rss=1'),
			(alL,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=33&rss=1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?RSS&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
