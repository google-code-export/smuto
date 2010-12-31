__plugin__  = "Onet.TV"
__author__  = "pajretX"
__date__    = "11-03-10"
__version__ = "0.03"


import sys
import xbmcaddon
Addon = xbmcaddon.Addon(id="plugin.video.onettv.pl")

#
# Wiadomości
#
if ( "wiado" in sys.argv[ 2 ] ):
	import resources.lib.wiadomosci as plugin
#
# Sport
#
elif ( "sport" in sys.argv[ 2 ] ):
    import resources.lib.sport as plugin
#
# Religia
#
elif ( "rel" in sys.argv[ 2 ] ):
    import resources.lib.religia as plugin
#
# Rozrywka
#
elif ( "rozr" in sys.argv[ 2 ] ):
    import resources.lib.rozrywka as plugin
#
# Muzyka
#
elif ( "muz" in sys.argv[ 2 ] ):
    import resources.lib.muzyka as plugin
#
# Film
#
elif ( "film" in sys.argv[ 2 ] ):
    import resources.lib.film as plugin
#
# Facet
#
elif ( "facet" in sys.argv[ 2 ] ):
    import resources.lib.facet as plugin
#
# Styl życia
#
elif ( "styl" in sys.argv[ 2 ] ):
    import resources.lib.styl as plugin
#
# Wnętrza
#
elif ( "wnet" in sys.argv[ 2 ] ):
    import resources.lib.wnetrza as plugin
#
# Zdrowie
#
elif ( "zdro" in sys.argv[ 2 ] ):
    import resources.lib.zdrowie as plugin
#
# Moto
#
elif ( "moto" in sys.argv[ 2 ] ):
    import resources.lib.moto as plugin
#
# Nowe Technologie
#
elif ( "nowe" in sys.argv[ 2 ] ):
    import resources.lib.nowe_technologie as plugin
#
# Biznes
#
elif ( "biz" in sys.argv[ 2 ] ):
    import  resources.lib.biznes as plugin
#
# Podróże
#
elif ( "pod" in sys.argv[ 2 ] ):
    import resources.lib.podroze as plugin
#
# Gry
#
elif ( "gry" in sys.argv[ 2 ] ):
    import resources.lib.gry as plugin
#
# Edukacja
#
elif ( "edu" in sys.argv[ 2 ] ):
    import resources.lib.edukacja as plugin
#
# RSS nazwy i inne takie..
#
elif ( "RSS" in sys.argv[ 2 ] ):
   import resources.lib.RSSszperator as plugin
#
# Odtwarzaj
#

else :
	import resources.lib.onet_main as plugin

plugin.Main()
