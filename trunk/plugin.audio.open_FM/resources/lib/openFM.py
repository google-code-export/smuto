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

__addon__   = "plugin.audio.open_FM"
__settings__ = xbmcaddon.Addon(id='plugin.audio.open_FM')

#
# Main class
#
class Main:
	def __init__( self ):
		
        #
        # Polecane
        #
		listitem = xbmcgui.ListItem( "Polecane", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1] ), url = '%s?pol&po_co=%s' % ( sys.argv[ 0 ], "Polecane" ), listitem=listitem, isFolder=True)		
        #
        # Impreza
        #
		listitem = xbmcgui.ListItem( "Impreza", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?impr&po_co=%s' % ( sys.argv[ 0 ], "Impreza" ), listitem=listitem, isFolder=True)
		#		
        # Pop
        #
		listitem = xbmcgui.ListItem( "Pop", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?pop&po_co=%s' % ( sys.argv[ 0 ], "Pop" ), listitem=listitem, isFolder=True)
        #
        # Hip-Hop/RnB
        #
		listitem = xbmcgui.ListItem( "Hip-Hop/RnB", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?hhrnb&po_co=%s' % ( sys.argv[ 0 ], "Hip-Hop/RnB" ), listitem=listitem, isFolder=True)
        #
        # Rock/Metal
        #
		listitem = xbmcgui.ListItem( "Rock/Metal", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?RM&po_co=%s' % ( sys.argv[ 0 ], "Rock/Metal" ), listitem=listitem, isFolder=True)
        #
        # Alternatywa
        #
		listitem = xbmcgui.ListItem( "Alternatywa", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?alt&po_co=%s' % ( sys.argv[ 0 ], "Alternatywa" ), listitem=listitem, isFolder=True)
        #
        # Sport
        #
		listitem = xbmcgui.ListItem( "Sport", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?sport&po_co=%s' % ( sys.argv[ 0 ], "Sport" ), listitem=listitem, isFolder=True)
        #
        # Elektronika
        #
		listitem = xbmcgui.ListItem( "Elektronika", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?elek&po_co=%s' % ( sys.argv[ 0 ], "Elektronika" ), listitem=listitem, isFolder=True)
        #
        # Do auta
        #
		listitem = xbmcgui.ListItem( "Do auta", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?auto&po_co=%s' % ( sys.argv[ 0 ], "Do auta" ), listitem=listitem, isFolder=True)
        #
        #  Inne
        #
		listitem = xbmcgui.ListItem( "Inne", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?inne&po_co=%s' % ( sys.argv[ 0 ], "Inne" ), listitem=listitem, isFolder=True)

        # Disable sorting...
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		
        # End of list...
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
