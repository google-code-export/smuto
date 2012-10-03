#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Imports
#
import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

__addon__   = "plugin.video.spryciarze.pl"
__settings__ = xbmcaddon.Addon(id='plugin.video.spryciarze.pl')

#
# Main class
#
class Main:
	def __init__( self ):
        
        #
        # Komputery
        #
		listitem = xbmcgui.ListItem( "Komputery", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1] ), url = '%s?kkk&po_co=%s' % ( sys.argv[ 0 ], "Komputery" ), listitem=listitem, isFolder=True)		
        
		#
        # Kulinaria
        #
		listitem = xbmcgui.ListItem( "Kulinaria", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?kulli&po_co=%s' % ( sys.argv[ 0 ], "Kulinaria" ), listitem=listitem, isFolder=True)
		
        #		
        # Kobieta
        #
		listitem = xbmcgui.ListItem( "Kobieta", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?kobbieta&po_co=%s' % ( sys.argv[ 0 ], "Kobieta" ), listitem=listitem, isFolder=True)

        #
        # Sport
        #
		listitem = xbmcgui.ListItem( "Sport", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?sp0rt&po_co=%s' % ( sys.argv[ 0 ], "Sport" ), listitem=listitem, isFolder=True)

        #
        # Dom i ogród
        #
		listitem = xbmcgui.ListItem( "Dom i ogród", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?domogr&po_co=%s' % ( sys.argv[ 0 ], "Dom i ogród" ), listitem=listitem, isFolder=True)

        #
        # Edukacja
        #
		listitem = xbmcgui.ListItem( "Edukacja", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?edu&po_co=%s' % ( sys.argv[ 0 ], "Edukacja" ), listitem=listitem, isFolder=True)
        
        #
        # Eksperymenty
        #
		listitem = xbmcgui.ListItem( "Eksperymenty", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?eksperymenty&po_co=%s' % ( sys.argv[ 0 ], "Eksperymenty" ), listitem=listitem, isFolder=True)

        #
        # Gadżety
        #
		listitem = xbmcgui.ListItem( "Gadżety", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?gadddz&po_co=%s' % ( sys.argv[ 0 ], "Gadżety" ), listitem=listitem, isFolder=True)
        
        #
        #  Hobby
        #
		listitem = xbmcgui.ListItem( "Hobby", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?hobbbby&po_co=%s' % ( sys.argv[ 0 ], "Hobby" ), listitem=listitem, isFolder=True)

        #
        #  Magia i sztuczki
        #
		listitem = xbmcgui.ListItem( "Magia i sztuczki", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?magi4&po_co=%s' % ( sys.argv[ 0 ], "Magia i sztuczki" ), listitem=listitem, isFolder=True)

        #
        #  Majsterkowanie
        #
		listitem = xbmcgui.ListItem( "Majsterkowanie", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?m4jst&po_co=%s' % ( sys.argv[ 0 ], "Majsterkowanie" ), listitem=listitem, isFolder=True)

        #
        #  Moda męska
        #
		listitem = xbmcgui.ListItem( "Moda męska", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?mmoda&po_co=%s' % ( sys.argv[ 0 ], "Moda męska" ), listitem=listitem, isFolder=True)

        #
        #  Motoryzacja
        #
		listitem = xbmcgui.ListItem( "Motoryzacja", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?mot0r&po_co=%s' % ( sys.argv[ 0 ], "Motoryzacja" ), listitem=listitem, isFolder=True)

        #
        #  Muzyka
        #
		listitem = xbmcgui.ListItem( "Muzyka", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?muzyka&po_co=%s' % ( sys.argv[ 0 ], "Muzyka" ), listitem=listitem, isFolder=True)

		#
		# Zdrowie
		#
		listitem = xbmcgui.ListItem( "Zdrowie", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?zdrowi3&po_co=%s' % ( sys.argv[ 0 ], "Zdrowie" ), listitem=listitem, isFolder=True)

		#
		# Różności
		#
		listitem = xbmcgui.ListItem( "Różności", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?rozn0&po_co=%s' % ( sys.argv[ 0 ], "Różności" ), listitem=listitem, isFolder=True)

		#
		# Sztuka i rzemiosło
		#
		listitem = xbmcgui.ListItem( "Sztuka i rzemiosło", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?sztuk4&po_co=%s' % ( sys.argv[ 0 ], "Sztuka i rzemiosło" ), listitem=listitem, isFolder=True)

		#
		# Telefony komórkowe
		#
		listitem = xbmcgui.ListItem( "Telefony komórkowe", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?telef0ny&po_co=%s' % ( sys.argv[ 0 ], "Telefony komórkowe" ), listitem=listitem, isFolder=True)
		
        #
        #  Survival
        #
		listitem = xbmcgui.ListItem( "Survival", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?surv1&po_co=%s' % ( sys.argv[ 0 ], "Survival" ), listitem=listitem, isFolder=True)

        # Sortowanie wyłączone
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		
        # Zakończenie listowania
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
