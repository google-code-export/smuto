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
			("Technika",'http://www.spryciarze.pl/kategorie/technika/page:1'),
			("Elektronika",'http://www.spryciarze.pl/kategorie/elektronika/page:1'),
			("Aparaty i kamery",'http://www.spryciarze.pl/kategorie/aparaty-i-kamery/page:1'),
			("Inne",'http://www.spryciarze.pl/kategorie/inne/page:1'),
			("Pirotechnika",'http://www.spryciarze.pl/kategorie/pirotechnika/page:1'),
			("Modelarstwo",'http://www.spryciarze.pl/kategorie/modelarstwo/page:1'),
			("Lego",'http://www.spryciarze.pl/kategorie/lego/page:1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?plej&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
