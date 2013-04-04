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
			("500 REGGAE HITS",'http://gr-relay-1.gaduradio.pl/30','http://open.fm/files/openfm/150x150_reggae_1.png'),
			("POLISH REGGAE STYLEE",'http://gr-relay-1.gaduradio.pl/22','http://open.fm/files/openfm/polishreggae.png'),
			("SKA ROOTS REGGAE",'http://gr-relay-1.gaduradio.pl/44','http://open.fm/files/openfm/skarootsreggae.png')
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
