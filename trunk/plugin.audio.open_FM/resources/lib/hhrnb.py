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
			("500 HIP-HOP HITS",'http://gr-relay-1.gaduradio.pl/84',os.path.join(ICO_DIR,'500_hip-hop_hits.png')),
			("HIP-HOP PL",'http://gr-relay-1.gaduradio.pl/24',os.path.join(ICO_DIR,'hip-hop_pl.png')),
			("HIP-HOP STACJA",'http://gr-relay-1.gaduradio.pl/23',os.path.join(ICO_DIR,'hhstacja.png')),
			("100% MAGIK",'http://gr-relay-1.gaduradio.pl/92',os.path.join(ICO_DIR,'magik.png')),
			("100% O.S.T.R",'http://gr-relay-1.gaduradio.pl/47',os.path.join(ICO_DIR,'OSTR.png')),
			("100% EMINEM",'http://gr-relay-1.gaduradio.pl/85','http://open.fm/files/openfm/100%%20eminem.png'),
			("500 R'n'B HITS",'http://gr-relay-1.gaduradio.pl/26',os.path.join(ICO_DIR,'500_RnB_hits.png')),
			("SOUL CAFÉ",'http://gr-relay-1.gaduradio.pl/18',os.path.join(ICO_DIR,'Soul_Cafe.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)