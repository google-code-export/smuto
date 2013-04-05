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
ICO_DIR = xbmc.translatePath( os.path.join( __settings__.getAddonInfo('path'), 'resources', 'ico' ) )

class Main:
	def __init__( self ) :
		self.getNames()
	def getNames(self):
		stos=[
			("500 ELECTRONIC HITS",'http://gr-relay-1.gaduradio.pl/94',os.path.join(ICO_DIR,'500_electronic.png')),
			("DRUM'N'BASS",'http://gr-relay-1.gaduradio.pl/41',os.path.join(ICO_DIR,'drumnbass.png')),
			("DUBSTEP",'http://gr-relay-1.gaduradio.pl/68',os.path.join(ICO_DIR,'dubstep_www.png')),
			("MINIMAL TECHNO",'http://gr-relay-1.gaduradio.pl/50',os.path.join(ICO_DIR,'minimal.png')),
			("CHILLOUT",'http://gr-relay-1.gaduradio.pl/33',os.path.join(ICO_DIR,'chill_out.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
