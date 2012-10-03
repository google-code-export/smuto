#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import urllib
import xbmcaddon

__addon__   = "plugin.video.spryciarze.pl"
__settings__ = xbmcaddon.Addon(id='plugin.video.spryciarze.pl')

class Main:
	def __init__( self ) :

		self.getNames()

	def getNames(self):
		gl=[
			("Karciane",'http://www.spryciarze.pl/kategorie/karciane/page:1'),
			("Iluzje",'http://www.spryciarze.pl/kategorie/iluzje/page:1'),
			("Tricki",'http://www.spryciarze.pl/kategorie/tricki/page:1'),
			("Zakłady",'http://www.spryciarze.pl/kategorie/zaklady/page:1'),
			("Psikusy",'http://www.spryciarze.pl/kategorie/psikusy/page:1'),
			("XCM",'http://www.spryciarze.pl/kategorie/xcm/page:1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?plej&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
