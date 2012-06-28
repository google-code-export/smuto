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
			("500 ALTERNATIVE HITS",'http://gr-relay-1.gaduradio.pl/55','http://open.fm/files/openfm/alternative_czarne_150x150.png'),
			("ALT FRESZZZ",'http://gr-relay-1.gaduradio.pl/6','http://open.fm/files/openfm/alt_fresh_150x150.png'),
			("ALT CLUB",'http://gr-relay-1.gaduradio.pl/9','http://open.fm/files/openfm/alt_club_150x150.png'),
			("ALT CAFÉ",'http://gr-relay-1.gaduradio.pl/34','http://open.fm/files/openfm/alt_cafe_150x150.png'),
			("ALT PL",'http://gr-relay-1.gaduradio.pl/36','http://open.fm/files/openfm/alt_pl_150x150.png')
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)

