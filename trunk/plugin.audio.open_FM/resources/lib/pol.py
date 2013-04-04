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
names = __settings__.getLocalizedString

class Main:
	def __init__( self ) :
		self.getNames()
	def getNames(self):
		stos=[
			("IMPREZA",'http://gr-relay-1.gaduradio.pl/2','http://open.fm/files/openfm/impreza_0.png'),
			("IMPREZA PL",'http://gr-relay-1.gaduradio.pl/12','http://open.fm/files/openfm/impreza_0.png'),
			("VIVA",'http://gr-relay-1.gaduradio.pl/64','http://openfm.festiwalmtv.pl/viva-2/images/logo_viva_radio.png'),
			("MTV",'http://gr-relay-1.gaduradio.pl/51','http://px.wporzo.pl/stuff/mtv.PNG'),
			("MTV ROCKS",'http://gr-relay-1.gaduradio.pl/77','http://open.fm/files/openfm/logo_mtv_rocks_radio_500x500_dostosowane_do_czarne_tlo1111.png'),
			("TOP 2012 Hits",'http://gr-relay-1.gaduradio.pl/93','http://open.fm/files/openfm/top_2012_150x150_na_biale_0.png'),
			("TOP 20 IMPREZA",'http://gr-relay-1.gaduradio.pl/95','http://open.fm/files/openfm/Top_20_Impreza_bialeTlo_150x150.png'),
			("TOP 20 DISCO POLO",'http://gr-relay-1.gaduradio.pl/53','http://open.fm/files/openfm/top20_discopolo_150x150_na_biale_0.png'),
			("TOP 20 POP",'http://gr-relay-1.gaduradio.pl/96','http://open.fm/files/openfm/Top_20_Pop_bialeTlo_150x150.png'),
			("TOP 20 PL",'http://gr-relay-1.gaduradio.pl/97','http://open.fm/files/openfm/Top_20_PL_bialeTlo_150x150_0.png'),
			("TOP 20 HIP-HOP",'http://gr-relay-1.gaduradio.pl/98','http://open.fm/files/openfm/Top_20_HH_bialeTlo_150x150.png'),
			("TOP 20 ROCK",'http://gr-relay-1.gaduradio.pl/99','http://open.fm/files/openfm/Top_20_Rock_bialeTlo_150x150.png')
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)