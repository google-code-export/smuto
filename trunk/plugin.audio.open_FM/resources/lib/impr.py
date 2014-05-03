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
			("Impreza",'http://gr-relay-12.gaduradio.pl/2',os.path.join(ICO_DIR,'impreza.png')),
			("Impreza PL",'http://gr-relay-12.gaduradio.pl/12',os.path.join(ICO_DIR,'impreza_pl.png')),
			("Top 20 Impreza",'http://gr-relay-12.gaduradio.pl/95',os.path.join(ICO_DIR,'top_20_impreza.png')),
			("Top 20 Disco Polo",'http://gr-relay-12.gaduradio.pl/53',os.path.join(ICO_DIR,'top_20_disco-polo.png')),
			("500 Party Hits",'http://gr-relay-12.gaduradio.pl/81',os.path.join(ICO_DIR,'500_party.png')),
			("Lejdis Party",'http://gr-relay-12.gaduradio.pl/102',os.path.join(ICO_DIR,'lejdis.png')),
			("Dance",'http://gr-relay-12.gaduradio.pl/31',os.path.join(ICO_DIR,'dance.png')),			
			("Trance",'http://gr-relay-12.gaduradio.pl/7',os.path.join(ICO_DIR,'trance.png')),
			("House",'http://gr-relay-12.gaduradio.pl/5',os.path.join(ICO_DIR,'house.png')),
			("Wesele",'http://gr-relay-12.gaduradio.pl/110',os.path.join(ICO_DIR,'wesele.png')),
			("Disco Polo",'http://gr-relay-12.gaduradio.pl/21',os.path.join(ICO_DIR,'disco-polo.png')),
			("Disco Polo Classic",'http://gr-relay-12.gaduradio.pl/49',os.path.join(ICO_DIR,'disco_polo_classic.png')),
			("Disco Polo Freszzz",'http://gr-relay-12.gaduradio.pl/57',os.path.join(ICO_DIR,'disco_polo_freszzz.png')),
			("Klub 90",'http://gr-relay-12.gaduradio.pl/8',os.path.join(ICO_DIR,'klub90.png')),
			("Italo Disco",'http://gr-relay-12.gaduradio.pl/27',os.path.join(ICO_DIR,'italo_disco.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
