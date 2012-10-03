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
			("Sony-Ericsson",'http://komputery.spryciarze.pl/kategorie/sony-ericsson/page:1'),
			("Nokia",'http://komputery.spryciarze.pl/kategorie/nokia/page:1'),
			("Samsung",'http://komputery.spryciarze.pl/kategorie/samsung/page:1'),
			("Przydatne strony",'http://komputery.spryciarze.pl/kategorie/gsm-przydatne-strony/page:1'),
			("Gry i programy",'http://komputery.spryciarze.pl/kategorie/gry-i-programy-na-telefon/page:1'),
			("iPhone",'http://komputery.spryciarze.pl/kategorie/iphone/page:1'),
			("Inni producenci",'http://komputery.spryciarze.pl/kategorie/inni-producenci/page:1'),
			("Modyfikacje i naprawy",'http://komputery.spryciarze.pl/kategorie/modyfikacje-i-naprawy/page:1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?plej&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
