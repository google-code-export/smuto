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
			("VIVA",'http://gr-relay-12.gaduradio.pl/64',os.path.join(ICO_DIR,'viva.png')),
			("MTV",'http://gr-relay-12.gaduradio.pl/51',os.path.join(ICO_DIR,'mtv.png')),
			("Praca",'http://gr-relay-12.gaduradio.pl/109',os.path.join(ICO_DIR,'praca.png')),
			("Nauka",'http://gr-relay-12.gaduradio.pl/117',os.path.join(ICO_DIR,'nauka.png')),
			("Relaks",'http://gr-relay-12.gaduradio.pl/112',os.path.join(ICO_DIR,'relaks.png')),
			("100% Justin Timberlake",'http://gr-relay-12.gaduradio.pl/103',os.path.join(ICO_DIR,'justin.png')),
			("Top 20 Pop",'http://gr-relay-12.gaduradio.pl/96',os.path.join(ICO_DIR,'top_20_pop.png')),
			("Top 20 PL",'http://gr-relay-12.gaduradio.pl/97',os.path.join(ICO_DIR,'top_20_pl.png')),
			("Top Hits 2013",'http://gr-relay-12.gaduradio.pl/44',os.path.join(ICO_DIR,'hits_2013.png')),
			("500 Największych Hitów",'http://gr-relay-12.gaduradio.pl/11',os.path.join(ICO_DIR,'500_big_hits.png')),
			("500 Pop Hits",'http://gr-relay-12.gaduradio.pl/83',os.path.join(ICO_DIR,'500_pop_hits.png')),
			("500 OMG Hits",'http://gr-relay-12.gaduradio.pl/105',os.path.join(ICO_DIR,'500_omg_hits.png')),
			("Freszzz",'http://gr-relay-12.gaduradio.pl/39',os.path.join(ICO_DIR,'freszzz.png')),
			("Po Polsku",'http://gr-relay-12.gaduradio.pl/1',os.path.join(ICO_DIR,'po_polsku.png')),
			("Po Polsku Classic",'http://gr-relay-12.gaduradio.pl/79',os.path.join(ICO_DIR,'po_polsku_class.png')),
			("Po Polsku Classic 2",'http://gr-relay-12.gaduradio.pl/17',os.path.join(ICO_DIR,'po_polsku_class2.png')),
			("Lejdis Café",'http://gr-relay-12.gaduradio.pl/48',os.path.join(ICO_DIR,'lejdis_caf.png')),
			("Crema Café",'http://gr-relay-12.gaduradio.pl/76',os.path.join(ICO_DIR,'crema_caf.png')),
			("Hity z Filmów i Seriali",'http://gr-relay-12.gaduradio.pl/58',os.path.join(ICO_DIR,'hity_seriale.png')),
			("We Dwoje",'http://gr-relay-12.gaduradio.pl/4',os.path.join(ICO_DIR,'we_dwoje.png')),
			("Ballady Wszech Czasów",'http://gr-relay-12.gaduradio.pl/20',os.path.join(ICO_DIR,'ballady_WC.png')),
			("100% Michael Jackson",'http://gr-relay-12.gaduradio.pl/10',os.path.join(ICO_DIR,'mj.png')),
			("100% Rihanna",'http://gr-relay-12.gaduradio.pl/86',os.path.join(ICO_DIR,'rih.png')),
			("Lation",'http://gr-relay-12.gaduradio.pl/19',os.path.join(ICO_DIR,'latino.png')),
			("Teens",'http://gr-relay-12.gaduradio.pl/69',os.path.join(ICO_DIR,'teens.png')),			
			("100% Justin Bieber",'http://gr-relay-12.gaduradio.pl/63',os.path.join(ICO_DIR,'bieber.png')),			
			("100% One Direction",'http://gr-relay-12.gaduradio.pl/80',os.path.join(ICO_DIR,'one_d.png')),	
			("00s Hits",'http://gr-relay-12.gaduradio.pl/72',os.path.join(ICO_DIR,'00.png')),
			("90s Hits",'http://gr-relay-12.gaduradio.pl/14',os.path.join(ICO_DIR,'90.png')),
			("80s Hits",'http://gr-relay-12.gaduradio.pl/3',os.path.join(ICO_DIR,'80.png')),
			("60s & 70s Hits",'http://gr-relay-12.gaduradio.pl/56',os.path.join(ICO_DIR,'60i70.png')),
			("Classic Hits",'http://gr-relay-12.gaduradio.pl/46',os.path.join(ICO_DIR,'classic_hits.png'))
			]
		for name, url, grafa in stos:
			li=xbmcgui.ListItem(name, thumbnailImage=grafa)
			li.setInfo( type="Audio", infoLabels={ "Title": name } )
			li.setProperty('mimetype', 'application/octet-stream')
			xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, isFolder=False)
		xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)
		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
