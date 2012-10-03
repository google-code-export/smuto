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
			("Makijaż",'http://kobieta.spryciarze.pl/kategorie/makijaz/page:1'),
			("Włosy",'http://kobieta.spryciarze.pl/kategorie/wlosy/page:1'),
			("Dłonie i paznokcie",'http://kobieta.spryciarze.pl/kategorie/dlonie-i-paznokcie/page:1'),
			("Biżuteria i dodatki",'http://kobieta.spryciarze.pl/kategorie/bizuteria-i-dodatki/page:1'),
			("Kosmetyki",'http://kobieta.spryciarze.pl/kategorie/kosmetyki/page:1'),
			("Styl i moda",'http://kobieta.spryciarze.pl/kategorie/styl-i-moda/page:1'),
			("Rodzina",'http://kobieta.spryciarze.pl/kategorie/rodzina/page:1'),
			("Związek i uczucia",'http://kobieta.spryciarze.pl/kategorie/zwiazek-i-uczucia/page:1'),
			("Zdrowie",'http://www.spryciarze.pl/kategorie/zdrowie/page:1'),
			("Nauka tańca",'http://www.spryciarze.pl/kategorie/taniec/page:1'),
			("Sport i fitness",'http://sport.spryciarze.pl/kategorie/kulturystyka-i-fitness/page:1'),
			("Dom i ogród",'http://www.spryciarze.pl/kategorie/dom-i-ogrod/page:1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?plej&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
