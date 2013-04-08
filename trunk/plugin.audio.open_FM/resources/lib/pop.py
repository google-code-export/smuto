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
			("500 NAJWIĘKSZYCH HITÓW",'http://gr-relay-1.gaduradio.pl/11',os.path.join(ICO_DIR,'500_best_www.png')),
			("500 POP HITS",'http://gr-relay-1.gaduradio.pl/83',os.path.join(ICO_DIR,'500_pop_hits.png')),
			("FRESZZZ",'http://gr-relay-1.gaduradio.pl/39',os.path.join(ICO_DIR,'freszzz.png')),
			("PO POLSKU",'http://gr-relay-1.gaduradio.pl/1',os.path.join(ICO_DIR,'po_polsku.png')),
			("PO POLSKU CLASSIC",'http://gr-relay-1.gaduradio.pl/79',os.path.join(ICO_DIR,'po_polsku_classic.png')),
			("PO POLSKU CLASSIC 2",'http://gr-relay-1.gaduradio.pl/17',os.path.join(ICO_DIR,'po_polsku_classic_2.png')),
			("LEJDIS CAFÉ",'http://gr-relay-1.gaduradio.pl/48',os.path.join(ICO_DIR,'lejdis_cafe.png')),
			("CREMA CAFÉ",'http://gr-relay-1.gaduradio.pl/76',os.path.join(ICO_DIR,'crema_cafe.png')),
			("WE DWOJE",'http://gr-relay-1.gaduradio.pl/4',os.path.join(ICO_DIR,'we_dwoje.png')),
			("BALLADY WSZECH CZASÓW",'http://gr-relay-1.gaduradio.pl/20',os.path.join(ICO_DIR,'ballady_WC.png')),
			("100% MICHAEL JACKSON",'http://gr-relay-1.gaduradio.pl/10',os.path.join(ICO_DIR,'mj.png')),
			("100% RIHANNA",'http://gr-relay-1.gaduradio.pl/86',os.path.join(ICO_DIR,'rih.png')),
			("LATINO",'http://gr-relay-1.gaduradio.pl/19',os.path.join(ICO_DIR,'latino.png')),
			("TEENS",'http://gr-relay-1.gaduradio.pl/69',os.path.join(ICO_DIR,'teens.png')),
			("TEENS MOVIE",'http://gr-relay-1.gaduradio.pl/65',os.path.join(ICO_DIR,'Teens_Movie.png')),
			("100% JUSTIN BIEBER",'http://gr-relay-1.gaduradio.pl/63',os.path.join(ICO_DIR,'justin.png')),
			("00s HITS",'http://gr-relay-1.gaduradio.pl/72',os.path.join(ICO_DIR,'00.png')),
			("90s HITS",'http://gr-relay-1.gaduradio.pl/14',os.path.join(ICO_DIR,'90.png')),
			("80s HITS",'http://gr-relay-1.gaduradio.pl/3',os.path.join(ICO_DIR,'80.png')),
			("60s & 70s HITS",'http://gr-relay-1.gaduradio.pl/56',os.path.join(ICO_DIR,'60i70.png')),
			("CLASSIC HITS",'http://gr-relay-1.gaduradio.pl/46',os.path.join(ICO_DIR,'classic_hits.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
