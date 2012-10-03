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
			("Grafika",'http://komputery.spryciarze.pl/kategorie/grafika/page:1'),
			("Audio i Wideo",'http://komputery.spryciarze.pl/kategorie/audio-i-wideo/page:1'),
			("Pobieranie plików i filmów",'http://komputery.spryciarze.pl/kategorie/pobieranie-plikow-i-filmow/page:1'),
			("Internet",'http://komputery.spryciarze.pl/kategorie/internet/page:1'),
			("Konsole",'http://komputery.spryciarze.pl/kategorie/konsole/page:1'),
			("Obróbka plików",'http://komputery.spryciarze.pl/kategorie/obrobka-plikow/page:1'),
			("Systemy operacyjne",'http://komputery.spryciarze.pl/kategorie/systemy-operacyjne/page:1'),
			("Gry",'http://komputery.spryciarze.pl/kategorie/gry/page:1'),
			("Programowanie",'http://komputery.spryciarze.pl/kategorie/programowanie/page:1'),
			("Bezpieczeństwo",'http://komputery.spryciarze.pl/kategorie/bezpieczenstwo/page:1'),
			("Telefony komórkowe",'http://komputery.spryciarze.pl/kategorie/telefony-komorkowe/page:1'),
			("Modyfikacje",'http://komputery.spryciarze.pl/kategorie/modyfikacje/page:1'),
			("Pakiety biurowe",'http://komputery.spryciarze.pl/kategorie/pakiety-biurowe/page:1'),
			("Przydatne programy",'http://komputery.spryciarze.pl/kategorie/przydatne-programy/page:1'),
			("Psikusy i triki",'http://komputery.spryciarze.pl/kategorie/psikusy-i-triki/page:1'),
			("Recenzje i testy",'http://komputery.spryciarze.pl/kategorie/komputery-recenzje-i-testy/page:1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?plej&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
