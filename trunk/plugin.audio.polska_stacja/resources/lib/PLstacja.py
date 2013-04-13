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

__addon__   = "plugin.audio.polska_stacja"
__settings__ = xbmcaddon.Addon(id='plugin.audio.polska_stacja')

#
# Main class
#
class Main:
	def __init__( self ):
		
        #
        # Wszystkie
        #
		listitem = xbmcgui.ListItem( "Wszystkie", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1] ), url = '%s?wszystkie&http://www.polskastacja.pl/radio=%s' % ( sys.argv[ 0 ], "Wszystkie" ), listitem=listitem, isFolder=True)		
		#
        # Nowe
        #
		listitem = xbmcgui.ListItem( "Nowe", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_28.htm=%s' % ( sys.argv[ 0 ], "Nowe" ), listitem=listitem, isFolder=True)
		#		
        # Polskie
        #
		listitem = xbmcgui.ListItem( "Polskie", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_1.htm=%s' % ( sys.argv[ 0 ], "Polskie" ), listitem=listitem, isFolder=True)
        #
        # Pop
        #
		listitem = xbmcgui.ListItem( "Pop", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_2.htm=%s' % ( sys.argv[ 0 ], "Pop" ), listitem=listitem, isFolder=True)
        #
        # Dance / DJ
        #
		listitem = xbmcgui.ListItem( "Dance / DJ", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_10.htm=%s' % ( sys.argv[ 0 ], "Dance / DJ" ), listitem=listitem, isFolder=True)
        #
        # Rock
        #
		listitem = xbmcgui.ListItem( "Rock", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_13.htm=%s' % ( sys.argv[ 0 ], "Rock" ), listitem=listitem, isFolder=True)
        #
        # Nowości
        #
		listitem = xbmcgui.ListItem( "Nowości", iconImage="DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_14.htm=%s' % ( sys.argv[ 0 ], "Nowości" ), listitem=listitem, isFolder=True)
        #
        # Przeboje
        #
		listitem = xbmcgui.ListItem( "Przeboje", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_15.htm=%s' % ( sys.argv[ 0 ], "Przeboje" ), listitem=listitem, isFolder=True)
        #
        #  Czarna Muza
        #
		listitem = xbmcgui.ListItem( "Czarna Muza", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_16.htm=%s' % ( sys.argv[ 0 ], "Czarna Muza" ), listitem=listitem, isFolder=True)
        #
        #  Elektronika
        #
		listitem = xbmcgui.ListItem( "Elektronika", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_17.htm=%s' % ( sys.argv[ 0 ], "Elektronika" ), listitem=listitem, isFolder=True)

        #
        #  Folk
        #
		listitem = xbmcgui.ListItem( "Folk", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_18.htm=%s' % ( sys.argv[ 0 ], "Folk" ), listitem=listitem, isFolder=True)

        #
        #  Reggae
        #
		listitem = xbmcgui.ListItem( "Reggae", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_19.htm=%s' % ( sys.argv[ 0 ], "Reggae" ), listitem=listitem, isFolder=True)

        #
        #  Religijne
        #
		listitem = xbmcgui.ListItem( "Religijne", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_20.htm=%s' % ( sys.argv[ 0 ], "Religijne" ), listitem=listitem, isFolder=True)

        #
        #  Świat
        #
		listitem = xbmcgui.ListItem( "Świat", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_21.htm=%s' % ( sys.argv[ 0 ], "Świat" ), listitem=listitem, isFolder=True)

        #
        #  Klasyka
        #
		listitem = xbmcgui.ListItem( "Klasyka", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_22.htm=%s' % ( sys.argv[ 0 ], "Klasyka" ), listitem=listitem, isFolder=True)

        #
        #  Film
        #
		listitem = xbmcgui.ListItem( "Film", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_23.htm=%s' % ( sys.argv[ 0 ], "Film" ), listitem=listitem, isFolder=True)

        #
        #  Jazz
        #
		listitem = xbmcgui.ListItem( "Jazz", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_24.htm=%s' % ( sys.argv[ 0 ], "Jazz" ), listitem=listitem, isFolder=True)

        #
        #  Relaks
        #
		listitem = xbmcgui.ListItem( "Relaks", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_25.htm=%s' % ( sys.argv[ 0 ], "Relaks" ), listitem=listitem, isFolder=True)

        #
        #  Inne
        #
		listitem = xbmcgui.ListItem( "Inne", iconImage = "DefaultFolder.png" )
		xbmcplugin.addDirectoryItem( handle = int(sys.argv[ 1 ]), url = '%s?wszystkie&http://www.polskastacja.pl/radio/filter_27.htm=%s' % ( sys.argv[ 0 ], "Inne" ), listitem=listitem, isFolder=True)


        # Disable sorting...
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		
        # End of list...
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
