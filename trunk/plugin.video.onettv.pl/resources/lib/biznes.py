import sys
import xbmc
import xbmcgui
import xbmcplugin
import urllib
import xbmcaddon

Addon = xbmcaddon.Addon(id="plugin.video.onettv.pl")
names = Addon.getLocalizedString

rai = (names (30015))
alL = (names (33333))

class Main:
	def __init__( self ) :
		self.getNames()
	def getNames(self):
		gl=[
			(alL,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=11&rss=1'),
			("TVN",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=11&tags=%28TVN%29&rss=1'),
			("TVN24",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=11&tags=%28TVN24%29&rss=1'),
			("TVN CNBC",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=11&tags=%28TVN_CNBC%29&rss=1'),
			("TVN WARSZAWA",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=11&tags=%28TVN_Warszawa%29&rss=1'),
			("CNN",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=11&tags=%28CNN%29&rss=1'),
			("Reuters",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=11&tags=%28Reuters%29&rss=1'),
			("OnetBiznes",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=11&tags=%28OnetBiznes%29&rss=1'),
			("Deutsche Welle",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=11&tags=%28Deutsche_Welle%29&rss=1'),
			(rai,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=11&tags=%28Kolej_TV%29&rss=1'),
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?RSS&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
