import sys
import xbmc
import xbmcgui
import xbmcplugin
import urllib
import xbmcaddon

Addon = xbmcaddon.Addon(id="plugin.video.onettv.pl")
names = Addon.getLocalizedString

jez = (names (30016))
DIS = (names (30017))
DID = (names (30018))
alL = (names (33333))

class Main:
	def __init__( self ) :
		self.getNames()
	def getNames(self):
		gl=[
			(alL,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=10&rss=1'),
			(jez,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=10&tags=%28Nauka_j%C4%99zyk%C3%B3w%29&rss=1'),
			(DID,'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=10&tags=%28Czy_wiesz%29&rss=1'),
			("Da Vinci Learning",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=10&tags=%28Da_Vinci_Learning%29&rss=1'),
			("Korki TV",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=10&tags=%28Korki_TV%29&rss=1'),
			("Know it",'http://www.onet.tv/feed/getMoviesCategoryOrTagsDate,15,1,desc,movies.xml?category=10&tags=%28Know_it%29&rss=1')
			]
		for name, url in gl:
			li=xbmcgui.ListItem(name)
			u=sys.argv[0]+"?RSS&po_co="+"&url="+urllib.quote_plus(url)
			xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,li,True)
		xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
