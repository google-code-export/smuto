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
			("500 HIP-HOP HITS",'http://gr-relay-1.gaduradio.pl/84','http://open.fm/files/openfm/hh_500x500_bialewww.png'),
			("HIP-HOP PL",'http://gr-relay-1.gaduradio.pl/24','http://open.fm/files/openfm/hiphop_pl150x150.png'),
			("HIP-HOP STACJA",'http://gr-relay-1.gaduradio.pl/23','http://open.fm/files/openfm/hhstacja_0.png'),
			("SOUL & R'N'B",'http://gr-relay-1.gaduradio.pl/26','http://open.fm/files/openfm/rnb_www.png')
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)