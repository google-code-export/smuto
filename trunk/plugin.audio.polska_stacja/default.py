#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys, xbmcaddon

__plugin__  = "polska_stacja"
__author__  = "pajretX"
__date__    = "13-04-13"
__version__ = "1.0.1"
__settings__ = xbmcaddon.Addon(id='plugin.audio.polska_stacja')


LIB_DIR = xbmc.translatePath( os.path.join( __settings__.getAddonInfo('path'), 'resources', 'lib' ) )
sys.path.append (LIB_DIR)

#
# Wszystkie
#
if ( "wszystkie" in sys.argv[ 2 ] ):
	import wszystkie as plugin
#
# Odtwarzaj
#
else :
	import PLstacja as plugin

plugin.Main()
