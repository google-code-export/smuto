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
			("VIVA",'http://gr-relay-12.gaduradio.pl/64',os.path.join(ICO_DIR,'viva.png')),
			("MTV",'http://gr-relay-12.gaduradio.pl/51',os.path.join(ICO_DIR,'mtv.png')),
			("MTV Rocks",'http://gr-relay-12.gaduradio.pl/77',os.path.join(ICO_DIR,'mtv_rocks.png')),
			("Impreza PL",'http://gr-relay-12.gaduradio.pl/12',os.path.join(ICO_DIR,'impreza_pl.png')),
			("Praca",'http://gr-relay-12.gaduradio.pl/109',os.path.join(ICO_DIR,'praca.png')),
			("Nauka",'http://gr-relay-12.gaduradio.pl/117',os.path.join(ICO_DIR,'nauka.png')),
			("Relaks",'http://gr-relay-12.gaduradio.pl/112',os.path.join(ICO_DIR,'relaks.png')),
			("Do Auta Rock",'http://gr-relay-12.gaduradio.pl/113',os.path.join(ICO_DIR,'auto_rock.png')),
			("Do Auta Club",'http://gr-relay-12.gaduradio.pl/114',os.path.join(ICO_DIR,'auto_club.png')),
			("Do Auta Hip-Hop",'http://gr-relay-12.gaduradio.pl/115',os.path.join(ICO_DIR,'auto_hh.png')),
			("100% Beyonce",'http://gr-relay-12.gaduradio.pl/111',os.path.join(ICO_DIR,'beyonce.png')),
			("100% Justin Timberlake",'http://gr-relay-12.gaduradio.pl/103',os.path.join(ICO_DIR,'justin.png')),			
			("Top 20 Impreza",'http://gr-relay-12.gaduradio.pl/95',os.path.join(ICO_DIR,'top_20_impreza.png')),
			("Top 20 Disco Polo",'http://gr-relay-12.gaduradio.pl/53',os.path.join(ICO_DIR,'top_20_disco-polo.png')),
			("Top 20 Pop",'http://gr-relay-12.gaduradio.pl/96',os.path.join(ICO_DIR,'top_20_pop.png')),
			("Top 20 PL",'http://gr-relay-12.gaduradio.pl/97',os.path.join(ICO_DIR,'top_20_pl.png')),
			("Top 20 Hip-Hop",'http://gr-relay-12.gaduradio.pl/98',os.path.join(ICO_DIR,'top_20_hip-hop.png')),
			("Top 20 Rock",'http://gr-relay-12.gaduradio.pl/99',os.path.join(ICO_DIR,'top_20_rock.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)