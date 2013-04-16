'''
    ekstraklasa.tv XBMC Plugin
    Copyright (C) 2012 smuto

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import elementtree.ElementTree as ET
import re,string
import urllib,urllib2
import xbmc, xbmcgui, xbmcplugin

plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    obrazek = img.replace("C", "D")
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=obrazek, 
                                thumbnailImage=obrazek)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=True)

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
                                
    return param
    
params=get_params()
akcja=None
url=None
xx=None
xxd=None

try:
    akcja=params["akcja"]
except:
    pass
try:
    url=urllib.unquote_plus(params["url"])
except:
    pass
try:
    xx=int(params["xx"])
except:
    pass
try:
    xxd=int(params["xxd"])
except:
    pass
print "akcja: "+str(akcja)
print "URL: "+str(url)
print "xx: "+str(xx)
print "xxd: "+str(xxd)

if akcja == 'seria':
    xml = urllib2.urlopen('http://serwisy.gazeta.pl/WideoSeria/0,0.html?xx=%d&xxd=%d' % (xx,xxd))
    data = ET.parse(xml).getroot()
    try:
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playList.clear()
        m = data.findall("m")
        for movie in m:
            title = movie.find('t').text
            img = movie.find('f').text
            print img
            listitem = xbmcgui.ListItem(title, thumbnailImage=img)
            url = movie.find('hq').text
            if not url:
                url = movie.find('p').text
            playList.add(url,listitem) 
        xbmc.Player().play(playList)
    except:
        pass

if akcja == 'graj':
    xml = urllib2.urlopen('http://serwisy.gazeta.pl/getDaneWideo?xx=%d&xxd=%d' % (xx,xxd))
    data = ET.parse(xml).getroot()
    try:
        m = data.findall("m")
        for movie in m:
            title = movie.find('t').text
            img = movie.find('f').text
            print img
            listitem = xbmcgui.ListItem(title, thumbnailImage=img)
            url = movie.find('hq').text
            if not url:
                url = movie.find('p').text
        xbmc.Player().play(url,listitem)
    except:
        pass

elif akcja == 'listuj':
    if '99215' in url:
        base_url = 'http://ekstraklasa.tv/ekstraklasa/0,'+url+'.html?str=%s'
        results = []
        for start in (0,1,2,3):
            url = base_url % (start)
            print url
            html = urllib2.urlopen(url).read()
            html = string.split(html,'class="serie_index"')
            if len(html)>=2:
                html = string.split(html[1],'class="pages"')
                html = string.split(html[0],'class="entry0"')
                for movie in html[1:]:
                    x = re.compile('<h2><a href=[^0-9]+[^,]+,([0-9]+),([0-9]+),[^>]+">([ \t\r\n]+)([^<]+)\n').findall(movie)[0]
                    date = re.compile('class="day">([^<]+)').findall(movie)[0]
                    img = re.compile('class="entry_img">[^>]+[^"]+"([^"]+)').findall(movie)[0]
                    nt = x + (date,img)
                    results.append(nt)
        for xxd, xx,nic, title,date, img in results:
            add_video_item(sys.argv[0]+"?akcja=seria&xxd="+str(xxd)+"&xx="+str(xx), {'title': '(%s) %s' % (date,title.decode('iso-8859-2') )}, img )
        xbmcplugin.endOfDirectory(plugin_handle) 
    elif not '99215' in url:
        xml = urllib2.urlopen('http://serwisy.gazeta.pl/WideoRss?dz=%s' % (url))
        data = ET.parse(xml).getroot()
        channel = data.findall("channel")[0]
        items = channel.findall("item")
        for item in items:
            title = item.find('title').text
            img = item.find('{http://search.yahoo.com/mrss/}content/{http://search.yahoo.com/mrss/}thumbnail').attrib.get('url')
            link = item.find('enclosure').attrib.get('url')
            xxd = re.search('xxd=([0-9]+)', link).group()
            xx = re.search('xx=([0-9]+)', link).group()
            add_video_item(sys.argv[0]+"?akcja=graj&"+str(xxd)+"&"+str(xx), {'title': '%s' % (title )}, img )
        xbmcplugin.endOfDirectory(plugin_handle) 


else:
    html = urllib2.urlopen('http://ekstraklasa.tv').read()
    html = string.split(html,'li id=\'e2\'')
    html = string.split(html[1],'li id=\'e3\'')
    html = string.split(html[0],'</a>')
    for kategoria in html[:-1]:
        href = re.compile('a href=\'[^,]+,([0-9]+)').findall(kategoria)[0]
        title = re.compile(' title=\'([^\']+)').findall(kategoria)[0]
        add_video_item(sys.argv[0]+"?akcja=listuj&url="+urllib.quote_plus(href), {'title': '%s' % (title.decode('iso-8859-2'))} )
    xbmcplugin.endOfDirectory(plugin_handle)
    
    

