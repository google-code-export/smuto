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
			("100% Beyonce",'http://gr-relay-12.gaduradio.pl/111',os.path.join(ICO_DIR,'beyonce.png')),
			("Top 20 Hip-Hop",'http://gr-relay-12.gaduradio.pl/98',os.path.join(ICO_DIR,'top_20_hip-hop.png')),
			("500 Hip-Hop Hits",'http://gr-relay-12.gaduradio.pl/84',os.path.join(ICO_DIR,'500_hhh.png')),
			("Hip-Hop PL",'http://gr-relay-12.gaduradio.pl/24',os.path.join(ICO_DIR,'hh_pl.png')),			
			("Hip-Hop Stacja",'http://gr-relay-12.gaduradio.pl/23',os.path.join(ICO_DIR,'hhstacja.png')),
			("Hip-Hop Freszzz",'http://gr-relay-12.gaduradio.pl/93',os.path.join(ICO_DIR,'hh_freszzz.png')),
			("Hip-Hop Klasyk",'http://gr-relay-12.gaduradio.pl/107',os.path.join(ICO_DIR,'hh_klasyk.png')),
			("Hip-Hop WWA",'http://gr-relay-12.gaduradio.pl/104',os.path.join(ICO_DIR,'hh_wwa.png')),			
			("100% Magik",'http://gr-relay-12.gaduradio.pl/92',os.path.join(ICO_DIR,'magik.png')),
			("100% O.S.T.R",'http://gr-relay-12.gaduradio.pl/47',os.path.join(ICO_DIR,'OSTR.png')),
			("100% Eminem",'http://gr-relay-12.gaduradio.pl/85',os.path.join(ICO_DIR,'eminem.png')),
			("500 R'n'B Hits",'http://gr-relay-12.gaduradio.pl/26',os.path.join(ICO_DIR,'500_RnB_hits.png')),
			("Soul Café",'http://gr-relay-12.gaduradio.pl/18',os.path.join(ICO_DIR,'Soul_Cafe.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)