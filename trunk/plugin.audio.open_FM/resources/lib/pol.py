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
			("IMPREZA",'http://gr-relay-1.gaduradio.pl/2',os.path.join(ICO_DIR,'impreza.png')),
			("IMPREZA PL",'http://gr-relay-1.gaduradio.pl/12',os.path.join(ICO_DIR,'impreza_pl.png')),
			("VIVA",'http://gr-relay-1.gaduradio.pl/64',os.path.join(ICO_DIR,'viva.png')),
			("MTV",'http://gr-relay-1.gaduradio.pl/51','http://px.wporzo.pl/stuff/mtv.PNG'),
			("MTV ROCKS",'http://gr-relay-1.gaduradio.pl/77',os.path.join(ICO_DIR,'mtv_rocks.png')),
			("TOP 2012 Hits",'http://gr-relay-1.gaduradio.pl/93',os.path.join(ICO_DIR,'top_2012_hits.png')),
			("TOP 20 IMPREZA",'http://gr-relay-1.gaduradio.pl/95',os.path.join(ICO_DIR,'top_20_impreza.png')),
			("TOP 20 DISCO POLO",'http://gr-relay-1.gaduradio.pl/53',os.path.join(ICO_DIR,'top_20_disco-polo.png')),
			("TOP 20 POP",'http://gr-relay-1.gaduradio.pl/96',os.path.join(ICO_DIR,'top_20_pop.png')),
			("TOP 20 PL",'http://gr-relay-1.gaduradio.pl/97',os.path.join(ICO_DIR,'top_20_pl.png')),
			("TOP 20 HIP-HOP",'http://gr-relay-1.gaduradio.pl/98',os.path.join(ICO_DIR,'top_20_hip-hop.png')),
			("TOP 20 ROCK",'http://gr-relay-1.gaduradio.pl/99',os.path.join(ICO_DIR,'top_20_rock.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)