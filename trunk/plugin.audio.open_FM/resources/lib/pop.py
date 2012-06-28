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
			("500 POP HITS",'http://gr-relay-1.gaduradio.pl/83','http://open.fm/files/openfm/pop_500x500_0.png'),
			("FRESZZZ",'http://gr-relay-1.gaduradio.pl/39','http://open.fm/files/openfm/fresz.png'),
			("PO POLSKU",'http://gr-relay-1.gaduradio.pl/1','http://open.fm/files/openfm/po_polsku_150x1502.png'),
			("PO POLSKU CLASSIC",'http://gr-relay-1.gaduradio.pl/79','http://open.fm/files/openfm/po_polsku_150x1502_classic_1_2.png'),
			("PO POLSKU CLASSIC 2",'http://gr-relay-1.gaduradio.pl/17','http://open.fm/files/openfm/po_polsku_150x150_classic_2_2.png'),
			("LEJDIS CAFÉ",'http://gr-relay-1.gaduradio.pl/48','http://open.fm/files/openfm/lejdis_500x500_biale.png'),
			("CREMA CAFÉ",'http://gr-relay-1.gaduradio.pl/76','http://open.fm/files/openfm/crema_square.png'),
			("WE DWOJE",'http://gr-relay-1.gaduradio.pl/4','http://open.fm/files/openfm/wedwoje_0.png'),
			("BALLADY WSZECH CZASÓW",'http://gr-relay-1.gaduradio.pl/20','http://open.fm/files/openfm/ballady.png'),
			("100% MICHAEL JACKSON",'http://gr-relay-1.gaduradio.pl/10','http://open.fm/files/openfm/mj_115x83.png'),
			("LATINO",'http://gr-relay-1.gaduradio.pl/19','http://open.fm/files/openfm/latino_0.png'),
			("TEENS",'http://gr-relay-1.gaduradio.pl/69','http://open.fm/files/openfm/teens_www_0.png'),
			("100% JUSTIN BIEBER",'http://gr-relay-1.gaduradio.pl/63','http://open.fm/files/openfm/100justin_www_0.png'),
			("00s HITS",'http://gr-relay-1.gaduradio.pl/72','http://open.fm/files/openfm/00_150x150_white.png'),
			("90s HITS",'http://gr-relay-1.gaduradio.pl/14','http://open.fm/files/openfm/90_150x150_white.png'),
			("80s HITS",'http://gr-relay-1.gaduradio.pl/3','http://open.fm/files/openfm/80_150x150_white.png'),
			("60s & 70s HITS",'http://gr-relay-1.gaduradio.pl/56','http://open.fm/files/openfm/60i70_150x150_white.png'),
			("CLASSIC HITS",'http://gr-relay-1.gaduradio.pl/46','http://open.fm/files/openfm/classic_150x150_white.png')
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
