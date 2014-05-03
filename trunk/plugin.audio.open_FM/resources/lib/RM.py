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
			("MTV Rocks",'http://gr-relay-12.gaduradio.pl/77',os.path.join(ICO_DIR,'mtv_rocks.png')),
			("Top 20 Rock",'http://gr-relay-12.gaduradio.pl/99',os.path.join(ICO_DIR,'top_20_rock.png')),
			("500 Rock Hits",'http://gr-relay-12.gaduradio.pl/82',os.path.join(ICO_DIR,'500_rock_hits.png')),
			("Polski Rock",'http://gr-relay-12.gaduradio.pl/29',os.path.join(ICO_DIR,'polski_rock.png')),
			("Polski Rock Classic",'http://gr-relay-12.gaduradio.pl/45',os.path.join(ICO_DIR,'polski_rock_classic.png')),			
			("Rock Ballady",'http://gr-relay-12.gaduradio.pl/61',os.path.join(ICO_DIR,'rock_ballady.png')),
			("Classic Rock",'http://gr-relay-12.gaduradio.pl/32',os.path.join(ICO_DIR,'classic_rock.png')),
			("American Rock",'http://gr-relay-12.gaduradio.pl/40',os.path.join(ICO_DIR,'americanrock.png')),
			("Punk Rock",'http://gr-relay-12.gaduradio.pl/78',os.path.join(ICO_DIR,'punk_rock.png')),
			("500 Heavy Hits",'http://gr-relay-12.gaduradio.pl/54',os.path.join(ICO_DIR,'500_heavyhits.png')),
			("Classic Metal",'http://gr-relay-12.gaduradio.pl/108',os.path.join(ICO_DIR,'class_metal.png')),
			("Ciężkie Brzmienia",'http://gr-relay-12.gaduradio.pl/13',os.path.join(ICO_DIR,'ciezkie_b.png')),			
			("100% Dżem",'http://gr-relay-12.gaduradio.pl/15',os.path.join(ICO_DIR,'dzem.png')),
			("100% Grabaż",'http://gr-relay-12.gaduradio.pl/73',os.path.join(ICO_DIR,'Grabaz.png')),
			("100% Kazik",'http://gr-relay-12.gaduradio.pl/35',os.path.join(ICO_DIR,'Kazik.png')),
			("100% Metallica",'http://gr-relay-12.gaduradio.pl/62',os.path.join(ICO_DIR,'Metallica.png')),
			("100% Linkin Park",'http://gr-relay-12.gaduradio.pl/42',os.path.join(ICO_DIR,'linkinpark.png')),			
			("100% Depeche Mode",'http://gr-relay-12.gaduradio.pl/74',os.path.join(ICO_DIR,'DM.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
