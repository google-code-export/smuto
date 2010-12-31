import sys
import xbmc
import xbmcgui
import xbmcplugin
import urllib
import xbmcaddon

Addon = xbmcaddon.Addon(id="plugin.video.onettv.pl")
names = Addon.getLocalizedString

alL = (names (33333))

class Main:
	def __init__( self ) :
		self.getNames()
	def getNames(self):
		gl=[
			(alL,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=12&rss=1'),
			("MOTO TV",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=12&tags=%28Moto_TV%29&rss=1'),
			("Testy",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=12&tags=%28Testy%29&rss=1'),
			("Modele",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=12&tags=%28Modele%29&rss=1'),
			("Porady",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=12&tags=%28Porady%29&rss=1'),
			("Przejezdna24",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=12&tags=%28Przejezdna24%29&rss=1'),
                        ("Inne",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=12&tags=%28Inne%29&rss=1'),
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?RSS&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
