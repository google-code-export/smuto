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
			("Dania mięsne",'http://kulinaria.spryciarze.pl/kategorie/dania-miesne/page:1'),
			("Ciasta i desery",'http://kulinaria.spryciarze.pl/kategorie/ciasta-i-desery/page:1'),
			("Napoje i drinki",'http://kulinaria.spryciarze.pl/kategorie/napoje-i-drinki/page:1'),
			("Ryby i owoce morza",'http://kulinaria.spryciarze.pl/kategorie/ryby-i-owoce-morza/page:1'),
			("Ryż i makarony",'http://kulinaria.spryciarze.pl/kategorie/ryz-i-makarony/page:1'),
			("Sałatki i surówki",'http://kulinaria.spryciarze.pl/kategorie/salatki-i-surowki/page:1'),
			("Naleśniki i omlety",'http://kulinaria.spryciarze.pl/kategorie/nalesniki-i-omlety/page:1'),
			("Pizza i zapiekanki",'http://kulinaria.spryciarze.pl/kategorie/pizza-i-zapiekanki/page:1'),
			("Pierogi i kluski",'http://kulinaria.spryciarze.pl/kategorie/pierogi-i-kluski/page:1'),
			("Zupy",'http://kulinaria.spryciarze.pl/kategorie/zupy/page:1'),
			("Sosy",'http://kulinaria.spryciarze.pl/kategorie/sosy/page:1'),
			("Pieczywo",'http://kulinaria.spryciarze.pl/kategorie/pieczywo/page:1'),
			("Ser i nabiał",'http://kulinaria.spryciarze.pl/kategorie/ser-i-nabial/page:1'),
			("Potrawy z grilla",'http://kulinaria.spryciarze.pl/kategorie/potrawy-z-grilla/page:1'),
			("Dania specjalne",'http://kulinaria.spryciarze.pl/kategorie/dania-specjalne/page:1'),
			("Potrawy Świąteczne",'http://kulinaria.spryciarze.pl/kategorie/potrawy-swiateczne/page:1'),
			("Diety",'http://kulinaria.spryciarze.pl/kategorie/diety/page:1'),
			("Warzywa i owoce",'http://kulinaria.spryciarze.pl/kategorie/warzywa-i-owoce/page:1'),
			("Grzyby",'http://kulinaria.spryciarze.pl/kategorie/grzyby/page:1'),
			("Sprzęt kuchenny",'http://kulinaria.spryciarze.pl/kategorie/sprzet-kuchenny/page:1'),
			("Recenzje produktów",'http://kulinaria.spryciarze.pl/kategorie/recenzje-produktow/page:1'),
			("Inne",'http://kulinaria.spryciarze.pl/kategorie/inne-kulinaria/page:1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?plej&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
