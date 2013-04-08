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
			("500 ROCK HITS",'http://gr-relay-1.gaduradio.pl/82',os.path.join(ICO_DIR,'500_rock_hits.png')),
			("POLSKI ROCK",'http://gr-relay-1.gaduradio.pl/29',os.path.join(ICO_DIR,'polskirock.png')),
			("POLSKI ROCK CLASSIC",'http://gr-relay-1.gaduradio.pl/45',os.path.join(ICO_DIR,'polski_rock_classic.png')),
			("ROCK BALLADY",'http://gr-relay-1.gaduradio.pl/61',os.path.join(ICO_DIR,'rock_ballady.png')),
			("CLASSIC ROCK",'http://gr-relay-1.gaduradio.pl/32',os.path.join(ICO_DIR,'classic_rock.png')),
			("AMERICAN ROCK",'http://gr-relay-1.gaduradio.pl/40',os.path.join(ICO_DIR,'americanrock.png')),
			("PUNK ROCK",'http://gr-relay-1.gaduradio.pl/78',os.path.join(ICO_DIR,'punkrock_www.png')),
			("500 HEAVY HITS",'http://gr-relay-1.gaduradio.pl/54',os.path.join(ICO_DIR,'500_heavyhits.png')),
			("100% GRABAŻ",'http://gr-relay-1.gaduradio.pl/73',os.path.join(ICO_DIR,'Grabaz.png')),
			("100% DŻEM",'http://gr-relay-1.gaduradio.pl/15',os.path.join(ICO_DIR,'dzem.png')),
			("100% KAZIK",'http://gr-relay-1.gaduradio.pl/35',os.path.join(ICO_DIR,'Kazik.png')),
			("100% METALLICA",'http://gr-relay-1.gaduradio.pl/62',os.path.join(ICO_DIR,'Metallica.png')),
			("100% LINKIN PARK",'http://gr-relay-1.gaduradio.pl/42',os.path.join(ICO_DIR,'linkinpark.png')),			
			("100% DEPECHE MODE",'http://gr-relay-1.gaduradio.pl/74',os.path.join(ICO_DIR,'dm.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
