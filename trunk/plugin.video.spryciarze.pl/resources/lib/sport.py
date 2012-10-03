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
			("Sztuki walki",'http://sport.spryciarze.pl/kategorie/sztuki-walki/page:1'),
			("Kulturystyka i fitness",'http://sport.spryciarze.pl/kategorie/kulturystyka-i-fitness/page:1'),
			("Piłka nożna",'http://sport.spryciarze.pl/kategorie/pilka-nozna/page:1'),
			("Extremalne",'http://sport.spryciarze.pl/kategorie/extremalne/page:1'),
			("Akrobatyka",'http://sport.spryciarze.pl/kategorie/akrobatyka/page:1'),
			("Penspinning",'http://sport.spryciarze.pl/kategorie/penspinning/page:1'),
			("Kuglarstwo",'http://sport.spryciarze.pl/kategorie/kuglarstwo/page:1'),
			("Szachy",'http://sport.spryciarze.pl/kategorie/szachy/page:1'),
			("Snooker i bilard",'http://sport.spryciarze.pl/kategorie/snooker-i-bilard/page:1'),
			("Fingerboard",'http://sport.spryciarze.pl/kategorie/fingerboard/page:1'),
			("Parkour",'http://sport.spryciarze.pl/kategorie/parkour/page:1'),
			("Taniec",'http://www.spryciarze.pl/kategorie/taniec/page:1'),
			("Inne",'http://sport.spryciarze.pl/kategorie/inne-sport/page:1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?plej&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
