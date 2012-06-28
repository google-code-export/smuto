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
			("TOP SUMMER HITS",'http://gr-relay-1.gaduradio.pl/75','http://open.fm/files/openfm/tsh_www_0.png'),
			("HIP-HOP KEMP",'http://gr-relay-1.gaduradio.pl/18','http://open.fm/files/openfm/HHK_www.png'),
			("VIVA",'http://gr-relay-1.gaduradio.pl/64','http://openfm.festiwalmtv.pl/viva-2/images/logo_viva_radio.png'),
			("MTV",'http://gr-relay-1.gaduradio.pl/51','http://px.wporzo.pl/stuff/mtv.PNG'),
			("MTV ROCKS",'http://gr-relay-1.gaduradio.pl/77','http://open.fm/files/openfm/logo_mtv_rocks_radio_500x500_dostosowane_do_czarne_tlo1111.png'),
			("MAYDAY",'http://gr-relay-1.gaduradio.pl/80','http://open.fm/files/openfm/logo_MAYDAY_150x150.png'),
			("DISCO POLO",'http://gr-relay-1.gaduradio.pl/21','http://open.fm/files/openfm/DiscoPolo_logo_180x82.png'),
			("DISCO POLO FRESZZZ",'http://gr-relay-1.gaduradio.pl/57','http://open.fm/files/openfm/DiscoPoloFreszzz_logo_153x82.png'),
			("DISCO POLO CLASSIC",'http://gr-relay-1.gaduradio.pl/49','http://open.fm/files/openfm/DiscoPoloClassic_logo_155x82.png'),
			("500 NAJWIĘKSZYCH HITÓW",'http://gr-relay-1.gaduradio.pl/11','http://open.fm/files/openfm/500_best_www.png')
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)