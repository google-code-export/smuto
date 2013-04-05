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
			("500 PARTY HITS",'http://gr-relay-1.gaduradio.pl/81',os.path.join(ICO_DIR,'500_party_hits.png')),
			("DANCE",'http://gr-relay-1.gaduradio.pl/31',os.path.join(ICO_DIR,'dance.png')),
			("TRANCE",'http://gr-relay-1.gaduradio.pl/7',os.path.join(ICO_DIR,'trance.png')),
			("HOUSE",'http://gr-relay-1.gaduradio.pl/5',os.path.join(ICO_DIR,'house.png')),
			("MAYDAY",'http://gr-relay-1.gaduradio.pl/80',os.path.join(ICO_DIR,'mayday.png')),
			("DISCO POLO",'http://gr-relay-1.gaduradio.pl/21',os.path.join(ICO_DIR,'DiscoPolo.png')),
			("DISCO POLO FRESZZZ",'http://gr-relay-1.gaduradio.pl/57',os.path.join(ICO_DIR,'disco_polo_freszzz.png')),
			("DISCO POLO CLASIC",'http://gr-relay-1.gaduradio.pl/49',os.path.join(ICO_DIR,'disco_polo_classic.png')),			
			("KLUB 90",'http://gr-relay-1.gaduradio.pl/8',os.path.join(ICO_DIR,'klub90.png')),
			("ITALO DISCO",'http://gr-relay-1.gaduradio.pl/27',os.path.join(ICO_DIR,'italo_disco.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
