#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys, xbmcaddon

__plugin__  = "Open FM"
__author__  = "pajretX"
__date__    = "03-05-14"
__version__ = "1.2.4"
__settings__ = xbmcaddon.Addon(id='plugin.audio.open_FM')


LIB_DIR = xbmc.translatePath( os.path.join( __settings__.getAddonInfo('path'), 'resources', 'lib' ) )
sys.path.append (LIB_DIR)

#
# Polecane
#
if ( "pol" in sys.argv[ 2 ] ):
	import pol as plugin
#
# Impreza
#
elif ( "impr" in sys.argv[ 2 ] ):
    import impr as plugin
#
# Pop
#
elif ( "pop" in sys.argv[ 2 ] ):
    import pop as plugin
#
# Hip-Hop/RnB
#
elif ( "hhrnb" in sys.argv[ 2 ] ):
    import hhrnb as plugin
#
# Rock/Metal
#
elif ( "RM" in sys.argv[ 2 ] ):
    import RM as plugin
#
# Alternatywa
#
elif ( "alt" in sys.argv[ 2 ] ):
    import  alt as plugin
#
# Sport
#
elif ( "sport" in sys.argv[ 2 ] ):
    import sport as plugin
#
# Elektronika
#
elif ( "elek" in sys.argv[ 2 ] ):
    import elek as plugin
#
# Do auta
#
elif ( "auto" in sys.argv[ 2 ] ):
    import auto as plugin
#
# Inne
#
elif ( "inne" in sys.argv[ 2 ] ):
    import inne as plugin
#
# Odtwarzaj
#
else :
	import openFM as plugin

plugin.Main()
