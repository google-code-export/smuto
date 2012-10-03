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
			("Matematyka",'http://www.spryciarze.pl/kategorie/matematyka/page:1'),
			("Pierwsza pomoc",'http://www.spryciarze.pl/kategorie/pierwsza-pomoc/page:1'),
			("Kursy i szkolenia",'http://www.spryciarze.pl/kategorie/kursy-i-szkolenia/page:1'),
			("Pomoce naukowe",'http://www.spryciarze.pl/kategorie/pomoce-naukowe/page:1'),
			("Finanse",'http://www.spryciarze.pl/kategorie/finanse/page:1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?plej&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
