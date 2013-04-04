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
			("500 PARTY HITS",'http://gr-relay-1.gaduradio.pl/81','http://open.fm/files/openfm/party_500x500www.png'),
			("DANCE",'http://gr-relay-1.gaduradio.pl/31','http://open.fm/files/openfm/dance_na_site.png'),
			("TRANCE",'http://gr-relay-1.gaduradio.pl/7','http://open.fm/files/openfm/trance_ftb_1.png'),
			("HOUSE",'http://gr-relay-1.gaduradio.pl/5','http://open.fm/files/openfm/house150x150.png'),
			("MAYDAY",'http://gr-relay-1.gaduradio.pl/80','http://open.fm/files/openfm/logo_MAYDAY_150x150.png'),
			("DISCO POLO",'http://gr-relay-1.gaduradio.pl/21','http://open.fm/files/openfm/DiscoPolo_logo_180x82.png'),
			("DISCO POLO FRESZZZ",'http://gr-relay-1.gaduradio.pl/57','http://open.fm/files/openfm/DiscoPoloFreszzz_logo_153x82.png'),
			("DISCO POLO CLASIC",'http://gr-relay-1.gaduradio.pl/49','http://open.fm/files/openfm/DiscoPoloClassic_logo_155x82.png'),			
			("KLUB 90",'http://gr-relay-1.gaduradio.pl/8','http://open.fm/files/openfm/klub90_0.png'),
			("ITALO DISCO",'http://gr-relay-1.gaduradio.pl/27','http://open.fm/files/openfm/italodisco.png')
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
