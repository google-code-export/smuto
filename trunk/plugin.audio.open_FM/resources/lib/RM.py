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
			("500 ROCK HITS",'http://gr-relay-1.gaduradio.pl/82','http://open.fm/files/openfm/rock_500x500_bialewww_0.png'),
			("POLSKI ROCK",'http://gr-relay-1.gaduradio.pl/29','http://open.fm/files/openfm/polskirock_0.png'),
			("POLSKI ROCK CLASSIC",'http://gr-relay-1.gaduradio.pl/45','http://open.fm/files/openfm/polski_rock_classic_150x150.png'),
			("POP-ROCK ZONE",'http://gr-relay-1.gaduradio.pl/53','http://open.fm/files/openfm/rock_pop_www.png'),
			("ROCK BALLADY",'http://gr-relay-1.gaduradio.pl/61','http://open.fm/files/openfm/rock_ballady_www.png'),
			("CLASSIC ROCK",'http://gr-relay-1.gaduradio.pl/32','http://open.fm/files/openfm/classicrock_0.png'),
			("SOLÓWKI WSZECH CZASÓW",'http://gr-relay-1.gaduradio.pl/47','http://open.fm/files/openfm/solowki_czarne_150x150.png'),
			("AMERICAN ROCK",'http://gr-relay-1.gaduradio.pl/40','http://open.fm/files/openfm/americanrock_0.png'),
			("PUNK ROCK",'http://gr-relay-1.gaduradio.pl/78','http://open.fm/files/openfm/punkrock_www.png'),
			("500 HEAVY HITS",'http://gr-relay-1.gaduradio.pl/54','http://open.fm/files/openfm/heavyhits_czarne_150x150.png'),
			("CIĘŻKIE BRZMIENIA",'http://gr-relay-1.gaduradio.pl/13','http://open.fm/files/openfm/ciezkiebrzmienia_0.png'),
			("CASTLE PARTY",'http://gr-relay-1.gaduradio.pl/70','http://open.fm/files/openfm/LogoCP_www.png'),
			("BLUES'N'ROCK",'http://gr-relay-1.gaduradio.pl/43','http://open.fm/files/openfm/bluesnrock_0.png'),
			("100% DŻEM",'http://gr-relay-1.gaduradio.pl/15','http://open.fm/files/openfm/dzem.png'),
			("100% KAZIK",'http://gr-relay-1.gaduradio.pl/35','http://open.fm/files/openfm/100_Kazik_www.png'),
			("100% METALLICA",'http://gr-relay-1.gaduradio.pl/62','http://open.fm/files/openfm/Metallica_www.png'),
			("100% LINKIN PARK",'http://gr-relay-1.gaduradio.pl/42','http://open.fm/files/openfm/logo_czarne_100_linkinpark_150x150.png'),			
			("100% DEPECHE MODE",'http://gr-relay-1.gaduradio.pl/74','http://open.fm/files/openfm/dm_www_czarne.png')
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
