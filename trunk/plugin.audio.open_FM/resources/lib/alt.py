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
			("500 Alternative Hits",'http://gr-relay-12.gaduradio.pl/55',os.path.join(ICO_DIR,'500_alternative.png')),
			("Alt Freszzz",'http://gr-relay-12.gaduradio.pl/6',os.path.join(ICO_DIR,'alt_fresh.png')),
			("Alt Club",'http://gr-relay-12.gaduradio.pl/9',os.path.join(ICO_DIR,'alt_club.png')),
			("Alt Café",'http://gr-relay-12.gaduradio.pl/34',os.path.join(ICO_DIR,'alt_cafe.png')),
			("Alt PL",'http://gr-relay-12.gaduradio.pl/36',os.path.join(ICO_DIR,'alt_pl.png')),
			("Alt Classic",'http://gr-relay-12.gaduradio.pl/43',os.path.join(ICO_DIR,'alt_class.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)

