#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys, xbmcaddon

__plugin__  = "Open FM"
__author__  = "pajretX"
__date__    = "04-04-13"
__version__ = "1.2"
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
# Reggae
#
elif ( "reG" in sys.argv[ 2 ] ):
    import reG as plugin
#
# Elektronika
#
elif ( "elek" in sys.argv[ 2 ] ):
    import elek as plugin
#
# Jazz
#
elif ( "jazz" in sys.argv[ 2 ] ):
    import jazz as plugin
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
