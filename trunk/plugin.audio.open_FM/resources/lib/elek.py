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
			("500 ELECTRONIC HITS",'http://gr-relay-1.gaduradio.pl/94','http://open.fm/files/openfm/Electronic500x500_bia%C5%82eT%C5%82o.png'),
			("DRUM'N'BASS",'http://gr-relay-1.gaduradio.pl/41','http://open.fm/files/openfm/drumnbass.png'),
			("DUBSTEP",'http://gr-relay-1.gaduradio.pl/68','http://open.fm/files/openfm/dubstep_www.png'),
			("MINIMAL TECHNO",'http://gr-relay-1.gaduradio.pl/50','http://open.fm/files/openfm/minimalTechno150x150.png'),
			("CHILLOUT",'http://gr-relay-1.gaduradio.pl/33','http://open.fm/files/openfm/chill_out150x150.png')
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
