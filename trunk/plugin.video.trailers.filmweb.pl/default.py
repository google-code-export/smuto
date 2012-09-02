# -*- coding: utf-8 -*-
import urllib, urllib2, re, sys, random
import cookielib, os, string, cookielib, StringIO
import os, time, base64, logging, calendar
import xbmcaddon, xbmcplugin, xbmcgui

scriptID = 'plugin.video.trailers.filmweb.pl'
scriptname = "Trailery"
#ptv = xbmcaddon.Addon(scriptID)

#BASE_RESOURCE_PATH = os.path.join( os.getcwd(), "resources" )
#BASE_RESOURCE_PATH = os.path.join( ptv.getAddonInfo('path'), "resources" )
#sys.path.append( os.path.join( BASE_RESOURCE_PATH, "lib" ) )

class FilmWebTrailers:
  URL = 'http://www.filmweb.pl/trailers'
  BASE = 'http://www.filmweb.pl'
  HOST = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.18) Gecko/20110621 Mandriva Linux/1.9.2.18-0.1mdv2010.2 (2010.2) Firefox/3.6.18'
  TRAILERS = []
  CUR_COUNT = 0
  MIN_ID = 11214
  MAX_ID = 0
  
  def __init__(self):
    __addon__ = xbmcaddon.Addon(scriptID)
    os.path.join( __addon__.getAddonInfo('path'), "resources" )
    self.numOfNewestTrailers = __addon__.getSetting('numOfNewestTrailers')
    self.numOfRandomTrailers = __addon__.getSetting('numOfRandomTrailers')
    self.onlyHD = __addon__.getSetting('onlyHD')

  def loadNewestTrailers(self):
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'welcomeScreen=welcome_screen'))
    page = opener.open(self.URL).read()

    matches = list(set(re.compile('href="(/video/trailer/[^"]+)"').findall(page)))
    
    toLoad = int(self.numOfNewestTrailers)
    for trailerLink in matches:
      if toLoad == 0:
        break
      if self.parseTrailerPage(trailerLink):
        toLoad -= 1
      
  def loadOldRandomTrailers(self):
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'welcomeScreen=welcome_screen'))
    page = opener.open(self.URL).read()
    
    matches = list(set(re.compile('href="/video/trailer/[^"]+\-([0-9]+)"').findall(page)))
    for trailerLink in matches:
      if int(matches[0]) > self.MAX_ID:
        self.MAX_ID = int(matches[0])

    toLoad = int(self.numOfRandomTrailers)
    while toLoad > 0:
      if self.parseTrailerPage("/video/trailer/-" + str(random.randint(self.MIN_ID, self.MAX_ID))):
        toLoad -= 1
     
  def parseTrailerPage(self, trailerLink):
    try:
      opener = urllib2.build_opener()
      opener.addheaders.append(('Cookie', 'welcomeScreen=welcome_screen'))
      trailerPage = opener.open(self.BASE + trailerLink).read()
    except:
      return False

    trailerVideos = re.compile('\"([^"]*\.(720|1080)p\.mp4)\"' if self.onlyHD else '\"([^"]*\.([0-9]+)p\.mp4)\"').findall(trailerPage)
    trailerName = re.compile('"/film/[^"]+" class=entityTitle>([^<]+)').findall(trailerPage)
    trailerPoster = re.compile('poster:"([^"]+)\.0\.jpg"').findall(trailerPage)

    if len(trailerName) == 0:
      return False
      #trailerName = 'Nieznany'
    else:
      trailerName = trailerName[0]
    
    if len(trailerPoster) == 0:
      trailerPoster = 'DefaultVideo.png'
    else:
      trailerPoster = trailerPoster[0] + ".3.jpg"
    
    trailerVideos = sorted(trailerVideos, key=lambda trailerVideos: trailerVideos[1], reverse=True)
    for video in trailerVideos:
      if len(video) == 2:
        listitem=xbmcgui.ListItem(label=trailerName, iconImage=trailerPoster, thumbnailImage=trailerPoster)
        listitem.setProperty('IsPlayable', 'true')
        listitem.setProperty( "Video", "true" )
        listitem.setInfo(type='Video', infoLabels={ "Title": trailerName, })
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=video[0], listitem=listitem, isFolder=False)
        self.TRAILERS.append({"url": video[0], "title": trailerName, "item": listitem, "poster": trailerPoster})
        self.CUR_COUNT += 1
        return True
    return False

  def run(self):
    xbmcplugin.setContent(int(sys.argv[1]),'movies')
    random.shuffle(self.TRAILERS)

    playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playList.clear()
    
    for v in self.TRAILERS:
      playList.add(v["url"], v["item"])

    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    xbmc.executebuiltin('playlist.playoffset(video , 0)')
    
filmweb = FilmWebTrailers()
filmweb.loadNewestTrailers()
filmweb.loadOldRandomTrailers()
filmweb.run()

