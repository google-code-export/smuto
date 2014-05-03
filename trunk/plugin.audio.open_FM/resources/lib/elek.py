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
			("500 Electronic Hits",'http://gr-relay-12.gaduradio.pl/94',os.path.join(ICO_DIR,'500_electronic.png')),
			("Miejska Stacja",'http://gr-relay-12.gaduradio.pl/106',os.path.join(ICO_DIR,'miejska_stac')),
			("Dubstep",'http://gr-relay-12.gaduradio.pl/68',os.path.join(ICO_DIR,'dubstep.png')),
			("Drum'N'Bass",'http://gr-relay-12.gaduradio.pl/41',os.path.join(ICO_DIR,'drumnbass.png')),
			("Chillout",'http://gr-relay-12.gaduradio.pl/33',os.path.join(ICO_DIR,'chill_out.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
