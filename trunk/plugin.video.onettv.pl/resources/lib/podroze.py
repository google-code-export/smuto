import sys
import xbmc
import xbmcgui
import xbmcplugin
import urllib
import xbmcaddon

Addon = xbmcaddon.Addon(id="plugin.video.onettv.pl")
names = Addon.getLocalizedString

KRY = (names (30049))
akt = (names (30050))
eks = (names (30051))
WFY = (names (30052))
gos = (names (30053))
alL = (names (33333))

class Main:
	def __init__( self ) :
		self.getNames()
	def getNames(self):
		gl=[
			(alL,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=8&rss=1'),
			(KRY,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=8&tags=%28Kraje_i_regiony%29&rss=1'),
			(akt,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=8&tags=%28Aktywnie%29&rss=1'),
			("TV",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=8&tags=%28TV%29&rss=1'),
			(eks,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=8&tags=%28Ekstremalnie%29&rss=1'),
			(WFY,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=8&tags=%28Wasze_filmy%29&rss=1'),
			(gos,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=8&tags=%28Go%C5%9Bcie%29&rss=1'),
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?RSS&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
