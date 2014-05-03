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
			("500 Reggae Hits",'http://gr-relay-12.gaduradio.pl/30',os.path.join(ICO_DIR,'500_reg.png')),
			("Polish Reggae Stylee",'http://gr-relay-12.gaduradio.pl/22',os.path.join(ICO_DIR,'pol_reg.png')),
			("Retro Café",'http://gr-relay-12.gaduradio.pl/25',os.path.join(ICO_DIR,'retro_caf.png')),
			("Smooth Jazz",'http://gr-relay-12.gaduradio.pl/60',os.path.join(ICO_DIR,'smooth_jazz.png')),
			("Muzyka Klasyczna",'http://gr-relay-12.gaduradio.pl/67',os.path.join(ICO_DIR,'klasyczna.png')),
			("Muzyka Filmowa",'http://gr-relay-12.gaduradio.pl/38',os.path.join(ICO_DIR,'filmowa.png')),
			("Kraina Łagodności",'http://gr-relay-12.gaduradio.pl/37',os.path.join(ICO_DIR,'krainalagodnosci.png')),
			("Szanty",'http://gr-relay-12.gaduradio.pl/28',os.path.join(ICO_DIR,'szanty.png')),
			("Biesiada",'http://gr-relay-12.gaduradio.pl/59',os.path.join(ICO_DIR,'biesiada.png')),
			("Biesiada Śląska",'http://gr-relay-12.gaduradio.pl/66',os.path.join(ICO_DIR,'slaska.png')),
			("Kids",'http://gr-relay-12.gaduradio.pl/16',os.path.join(ICO_DIR,'kids.png')),
			("Odgłosy Natury",'http://gr-relay-12.gaduradio.pl/52',os.path.join(ICO_DIR,'natura.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
