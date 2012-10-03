#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import xbmcaddon

__plugin__  = "spryciarze.pl"
__author__  = "pajretX"
__date__    = "02-10-12"
__version__ = "1.0"
__addon__   = "plugin.video.spryciarze.pl"
__settings__ = xbmcaddon.Addon(id='plugin.video.spryciarze.pl')


LIB_DIR = xbmc.translatePath( os.path.join( __settings__.getAddonInfo('path'), 'resources', 'lib' ) )
sys.path.append (LIB_DIR)


#
# Komputery
#
if ( "kkk" in sys.argv[ 2 ] ):
	import komputery as plugin
#
# Kulinaria
#
elif ( "kulli" in sys.argv[ 2 ] ):
    import kulinaria as plugin
#
# Kobieta
#
elif ( "kobbieta" in sys.argv[ 2 ] ):
    import kobieta as plugin
#
# Sport
#
elif ( "sp0rt" in sys.argv[ 2 ] ):
    import sport as plugin
#
# Dom i ogród
#
elif ( "domogr" in sys.argv[ 2 ] ):
    import domogrod as plugin
#
# Edukacja
#
elif ( "edu" in sys.argv[ 2 ] ):
    import  edukacja as plugin
#
# Eksperymenty
#
elif ( "ekspe" in sys.argv[ 2 ] ):
   import eksperymenty as plugin
#
# Gadżety
#
elif ( "gadddz" in sys.argv[ 2 ] ):
    import gadzety as plugin
#
# Hobby
#
elif ( "hobbbby" in sys.argv[ 2 ] ):
    import hobby as plugin
#
# Magia i sztuczki
#
elif ( "magi4" in sys.argv[ 2 ] ):
    import magsztuczki as plugin
#
# Majsterkowanie
#
elif ( "m4jst" in sys.argv[ 2 ] ):
    import majsterkowanie as plugin
#
# Moda męska
#
elif ( "mmoda" in sys.argv[ 2 ] ):
    import mmoda as plugin
#
# Motoryzacja
#
elif ( "mot0r" in sys.argv[ 2 ] ):
    import motoryzacja as plugin
#
# Muzyka
#
elif ( "muzyka" in sys.argv[ 2 ] ):
    import muzyka as plugin
#
# Zdrowie
#
elif ( "zdrowi3" in sys.argv[ 2 ] ):
    import zdrowie as plugin
#
# Różności
#
elif ( "rozn0" in sys.argv[ 2 ] ):
    import roznosci as plugin
#
# Sztuka i rzemiosło
#
elif ( "sztuk4" in sys.argv[ 2 ] ):
    import sztuka as plugin
#
# Telefony komórkowe
#
elif ( "telef0ny" in sys.argv[ 2 ] ):
    import telefony as plugin
#
# Survival
#
elif ( "surv1" in sys.argv[ 2 ] ):
    import survival as plugin
#
# RSS nazwy i inne takie..
#
elif ( "plej" in sys.argv[ 2 ] ):
   import plejator as plugin
#
# Odtwarzaj
#
else :
	import spryt_main as plugin

plugin.Main()
