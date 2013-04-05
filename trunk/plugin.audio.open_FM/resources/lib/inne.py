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
			("MUZYKA KLASYCZNA",'http://gr-relay-1.gaduradio.pl/67',os.path.join(ICO_DIR,'klasyczna.png')),
			("MUZYKA FILMOWA",'http://gr-relay-1.gaduradio.pl/38',os.path.join(ICO_DIR,'filmowa.png')),
			("KRAINA ŁAGODNOŚCI",'http://gr-relay-1.gaduradio.pl/37',os.path.join(ICO_DIR,'krainalagodnosci.png')),
			("SZANTY",'http://gr-relay-1.gaduradio.pl/28',os.path.join(ICO_DIR,'szanty.png')),
			("BIESIADA",'http://gr-relay-1.gaduradio.pl/59',os.path.join(ICO_DIR,'biesiada.png')),
			("BIESIADA ŚLĄSKA",'http://gr-relay-1.gaduradio.pl/66',os.path.join(ICO_DIR,'slaska.png')),
			("KIDS",'http://gr-relay-1.gaduradio.pl/16',os.path.join(ICO_DIR,'kids.png')),
			("ODGŁOSY NATURY",'http://gr-relay-1.gaduradio.pl/52',os.path.join(ICO_DIR,'natura.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
