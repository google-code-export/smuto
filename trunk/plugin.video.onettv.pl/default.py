#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import xbmcaddon

__plugin__  = "Onet.TV"
__author__  = "pajretX"
__date__    = "06-04-2013"
__version__ = "1.0.3"
__addon__   = "plugin.video.onettv.pl"
__settings__ = xbmcaddon.Addon(id='plugin.video.onettv.pl')


LIB_DIR = xbmc.translatePath( os.path.join( __settings__.getAddonInfo('path'), 'resources', 'lib' ) )
sys.path.append (LIB_DIR)


#
# Wiadomości
#
if ( "wiado" in sys.argv[ 2 ] ):
	import wiadomosci as plugin
#
# Religia
#
elif ( "rel" in sys.argv[ 2 ] ):
    import religia as plugin
#
# Rozrywka
#
elif ( "rozr" in sys.argv[ 2 ] ):
    import rozrywka as plugin
#
# Film
#
elif ( "film" in sys.argv[ 2 ] ):
    import film as plugin
#
# Gry
#
elif ( "gry" in sys.argv[ 2 ] ):
    import gry as plugin
#
# Biznes
#
elif ( "biz" in sys.argv[ 2 ] ):
    import  biznes as plugin
#
# Gotowanie
#
#elif ( "got" in sys.argv[ 2 ] ):
#   import gotowanie as plugin
#
# Plejada talentów
#
#elif ( "plej" in sys.argv[ 2 ] ):
#    import plejada as plugin
#
# Sport
#
elif ( "sport" in sys.argv[ 2 ] ):
    import sport as plugin
#
# Styl życia
#
elif ( "styl" in sys.argv[ 2 ] ):
    import styl as plugin
#
# Muzyka
#
elif ( "muz" in sys.argv[ 2 ] ):
    import muzyka as plugin
#
# Podróże
#
elif ( "pod" in sys.argv[ 2 ] ):
    import podroze as plugin
#
# Edukacja
#
elif ( "edu" in sys.argv[ 2 ] ):
    import edukacja as plugin
#
# Moto
#
elif ( "moto" in sys.argv[ 2 ] ):
    import moto as plugin
#
# Facet
#
elif ( "facet" in sys.argv[ 2 ] ):
    import facet as plugin
#
# Wnetrza
#
elif ( "wnet" in sys.argv[ 2 ] ):
    import wnet as plugin
#
# Zdrowie
#
elif ( "zdro" in sys.argv[ 2 ] ):
    import zdro as plugin
#
# Nowe Technologie
#
elif ( "nowtech" in sys.argv[ 2 ] ):
    import nowtech as plugin
#
# Świat dziecka
#
#elif ( "swiat" in sys.argv[ 2 ] ):
#    import swiat as plugin
#
# RSS nazwy i inne takie..
#
elif ( "RSS" in sys.argv[ 2 ] ):
   import RSSszperator as plugin
#
# Odtwarzaj
#

else :
	import onet_main as plugin

plugin.Main()
