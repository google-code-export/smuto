#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import urllib
import xbmcaddon

__addon__   = "plugin.audio.open_FM"
__settings__ = xbmcaddon.Addon(id='plugin.audio.open_FM')
names = __settings__.getLocalizedString

class Main:
	def __init__( self ) :
		self.getNames()
	def getNames(self):
		stos=[
			("MUZYKA KLASYCZNA",'http://gr-relay-1.gaduradio.pl/67','http://open.fm/files/openfm/na_sajt.png'),
			("MUZYKA FILMOWA",'http://gr-relay-1.gaduradio.pl/38','http://open.fm/files/openfm/150x150_MuzykaFilmowa_1.png'),
			("KRAINA ŁAGODNOŚCI",'http://gr-relay-1.gaduradio.pl/37','http://open.fm/files/openfm/krainalagodnosci.png'),
			("SZANTY",'http://gr-relay-1.gaduradio.pl/28','http://open.fm/files/openfm/szanty_0.png'),
			("BIESIADA",'http://gr-relay-1.gaduradio.pl/59','http://open.fm/files/openfm/biesiada_www.png'),
			("BIESIADA ŚLĄSKA",'http://gr-relay-1.gaduradio.pl/66','http://open.fm/files/openfm/bsWWW.png'),
			("KIDS",'http://gr-relay-1.gaduradio.pl/16','http://open.fm/files/openfm/kids_0.png'),
			("ODGŁOSY NATURY",'http://gr-relay-1.gaduradio.pl/52','http://open.fm/files/openfm/odglosynatury.png')
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
