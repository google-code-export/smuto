'''
    sport.pl XBMC Plugin
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
    print obrazek
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
    #studio sport.pl
    if '0,0' in url:
        print 'studio sport.pl'
        base_url = url+'?str=%s_10617105'
        results = []
        for start in (1,2,3,4):
            url = base_url % (start)
            html = urllib2.urlopen(url).read()
            html = string.split(html,'id="col_left"')
            if len(html)>=2:
                html = string.split(html[1],'class="footer"')
                html = string.split(html[0],'div class="imgw"')
                for movie in html[1:]:
                    x = re.compile('href=[^0-9]+[^,]+,([0-9]+),([0-9]+),[^"]+">Obejrzyj wszystkie').findall(movie)[0]
                    title = re.compile('a title="([^"]+)').findall(movie)[0]
                    date = re.compile('class="when">([^ ]+)').findall(movie)[0]
                    img = re.compile('img src="([^"]+)').findall(movie)[0]
                    nt = x + (title,date,img)
                    results.append(nt)
        for xxd, xx, title,date, img in results:
            add_video_item(sys.argv[0]+"?akcja=seria&xxd="+str(xxd)+"&xx="+str(xx), {'title': '(%s) %s' % (date,title )}, img )
            xbmcplugin.endOfDirectory(plugin_handle)
    # magazyn extraklasy
    elif '99215' in url:
        print 'extra'
        base_url = url+'?str=%s'
        results = []
        for start in (0,1,2,3):
            url = base_url % (start)
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
            add_video_item(sys.argv[0]+"?akcja=seria&xxd="+str(xxd)+"&xx="+str(xx), {'title': '(%s) %s' % (date,title )}, img )
            xbmcplugin.endOfDirectory(plugin_handle) 
    # liga mistrzow i mma
    elif '112273' in url:
        print 'liga mistrzow'
        html = urllib2.urlopen(url).read()
        html = string.split(html,'id="col_left"')
        if len(html)>=2:
            html = string.split(html[1],'class="footer"')
            html = string.split(html[0],'div class="imgw"')
            for movie in html[1:]:
                x = re.compile('href=[^0-9]+[^,]+,([0-9]+),([0-9]+),[^"]+">Obejrzyj wszystkie').findall(movie)[0]
                title = re.compile('a title="([^"]+)').findall(movie)[0]
                date = re.compile('class="when">([^ ]+)').findall(movie)[0]
                img = re.compile('img src="([^"]+)').findall(movie)[0]
                add_video_item(sys.argv[0]+"?akcja=seria&xxd="+str(x[0])+"&xx="+str(x[1]), {'title': '(%s) %s' % (date,title )}, img )
                xbmcplugin.endOfDirectory(plugin_handle)
    elif '97841' in url:
        print 'liga mistrzow'
        html = urllib2.urlopen(url).read()
        html = string.split(html,'id="col_left"')
        if len(html)>=2:
            html = string.split(html[1],'class="footer"')
            html = string.split(html[0],'div class="imgw"')
            for movie in html[1:]:
                x = re.compile('href=[^0-9]+[^,]+,([0-9]+),([0-9]+),[^"]+">Obejrzyj wszystkie').findall(movie)[0]
                title = re.compile('a title="([^"]+)').findall(movie)[0]
                date = re.compile('class="when">([^ ]+)').findall(movie)[0]
                img = re.compile('img src="([^"]+)').findall(movie)[0]
                add_video_item(sys.argv[0]+"?akcja=seria&xxd="+str(x[0])+"&xx="+str(x[1]), {'title': '(%s) %s' % (date,title )}, img )
                xbmcplugin.endOfDirectory(plugin_handle) 
    # formula1
    elif '97844' in url:
        print 'formula1'
        base_url = url+'?str=%s_10617454'
        results = []
        for start in (1,2,3,4):
            url = base_url % (start)
            html = urllib2.urlopen(url).read()
            html = string.split(html,'id="col_left"')
            if len(html)>=2:
                html = string.split(html[1],'class="footer"')
                html = string.split(html[0],'div class="imgw"')
                for movie in html[1:]:
                    x = re.compile('href=[^0-9]+[^,]+,([0-9]+),([0-9]+),[^"]+">Obejrzyj wszystkie').findall(movie)[0]
                    title = re.compile('a title="([^"]+)').findall(movie)[0]
                    date = re.compile('class="when">([^ ]+)').findall(movie)[0]
                    img = re.compile('img src="([^"]+)').findall(movie)[0]
                    nt = x + (title,date,img)
                    results.append(nt)
        for xxd, xx, title,date, img in results:
            add_video_item(sys.argv[0]+"?akcja=seria&xxd="+str(xxd)+"&xx="+str(xx), {'title': '(%s) %s' % (date,title )}, img )
            xbmcplugin.endOfDirectory(plugin_handle)

    # siatkarski
    elif '97845' in url:
        print 'siatkarski'
        base_url = url+'?str=%s_10617629'
        results = []
        for start in (1,2,3,4):
            url = base_url % (start)
            html = urllib2.urlopen(url).read()
            html = string.split(html,'id="col_left"')
            if len(html)>=2:
                html = string.split(html[1],'class="footer"')
                html = string.split(html[0],'div class="imgw"')
                for movie in html[1:]:
                    x = re.compile('href=[^0-9]+[^,]+,([0-9]+),([0-9]+),[^"]+">Obejrzyj wszystkie').findall(movie)[0]
                    title = re.compile('a title="([^"]+)').findall(movie)[0]
                    date = re.compile('class="when">([^ ]+)').findall(movie)[0]
                    img = re.compile('img src="([^"]+)').findall(movie)[0]
                    nt = x + (title,date,img)
                    results.append(nt)
        for xxd, xx, title,date, img in results:
            add_video_item(sys.argv[0]+"?akcja=seria&xxd="+str(xxd)+"&xx="+str(xx), {'title': '(%s) %s' % (date,title )}, img )
            xbmcplugin.endOfDirectory(plugin_handle)

    # inne serie
    elif '98305' in url:
        print 'inne serie'
        base_url = url+'?str=%s_10617140'
        results = []
        for start in (1,2,3,4):
            url = base_url % (start)
            html = urllib2.urlopen(url).read()
            html = string.split(html,'id="col_left"')
            if len(html)>=2:
                html = string.split(html[1],'class="footer"')
                html = string.split(html[0],'div class="imgw"')
                for movie in html[1:]:
                    x = re.compile('href=[^0-9]+[^,]+,([0-9]+),([0-9]+),[^"]+">Obejrzyj wszystkie').findall(movie)[0]
                    title = re.compile('a title="([^"]+)').findall(movie)[0]
                    date = re.compile('class="when">([^ ]+)').findall(movie)[0]
                    img = re.compile('img src="([^"]+)').findall(movie)[0]
                    nt = x + (title,date,img)
                    results.append(nt)
        for xxd, xx, title,date, img in results:
            add_video_item(sys.argv[0]+"?akcja=seria&xxd="+str(xxd)+"&xx="+str(xx), {'title': '(%s) %s' % (date,title )}, img )
            xbmcplugin.endOfDirectory(plugin_handle)

    #wszystkie wideo
    elif '67450' in url:
        print 'wszystkie'
        base_url = url+'?str=%s_10699130'
        results = []
        for start in (1,2,3,4,5):
            url = base_url % (start)
            html = urllib2.urlopen(url).read()
            html = string.split(html,'id="col_left"')
            if len(html)>=2:
                html = string.split(html[1],'class="footer"')
                html = string.split(html[0],'div class="imgw"')
                for movie in html[1:]:
                    x = re.compile('title="([^"]+)" href=[^0-9]+[^,]+,([0-9]+),([0-9]+)').findall(movie)[0]
                    date = re.compile('class="when">([^ ]+)').findall(movie)[0]
                    try:
                        img = re.compile('img src="([^"]+)').findall(movie)[0]
                    except:
                        img=''
                        pass
                    nt = x + (date,img)
                    results.append(nt)
        for title, xxd, xx,date, img in results:
            add_video_item(sys.argv[0]+"?akcja=graj&xxd="+str(xxd)+"&xx="+str(xx), {'title': '(%s) %s' % (date,title )}, img )
            xbmcplugin.endOfDirectory(plugin_handle)





    '''
    html = urllib2.urlopen(url).read()
    html = string.split(html,'id="col_left"')
    if len(html)>=2:
        html = string.split(html[1],'class="footer"')
        html = string.split(html[0],'div class="imgw"')
        for movie in html[1:]:
            x = re.compile('href=[^0-9]+[^,]+,([0-9]+),([0-9]+),[^"]+">Obejrzyj wszystkie').findall(movie)[0]
            title = re.compile('a title="([^"]+)').findall(movie)[0]
            img = re.compile('img src="([^"]+)').findall(movie)[0]
            add_video_item(sys.argv[0]+"?akcja=seria&xxd="+str(x[0])+"&xx="+str(x[1]), {'title': '%s' % (title)}, img )
            xbmcplugin.endOfDirectory(plugin_handle)    

    print url
    base_url = 'http://www.sport.pl/video/0,0.html?str=%s_10617105'
    results = []
    for start in (1,2,3):
        url = base_url % (start)
        html = urllib2.urlopen(url).read()
        html = string.split(html,'id="col_left"')
        if len(html)>=2:
            html = string.split(html[1],'class="footer"')
            html = string.split(html[0],'div class="imgw"')
            for movie in html[1:]:
                x = re.compile('href=[^0-9]+[^,]+,([0-9]+),([0-9]+),[^"]+">Obejrzyj wszystkie').findall(movie)[0]
                title = re.compile('a title="([^"]+)').findall(movie)[0]
                img = re.compile('img src="([^"]+)').findall(movie)[0]
                nt = x + (title,img)
                results.append(nt)
    for xxd, xx, title, img in results:
        add_video_item(sys.argv[0]+"?akcja=odtwarzaj&xxd="+str(xxd)+"&xx="+str(xx), {'title': '%s' % (title)}, img )
        xbmcplugin.endOfDirectory(plugin_handle)
    '''
else:
    print ' kategorie'
    html = urllib2.urlopen('http://www.sport.pl').read()
    html = string.split(html,'li id=\'e11\'')
    html = string.split(html[1],'li id=\'e12\'')
    html = string.split(html[0],'</a>')
    for kategoria in html[:-1]:
        href = re.compile('a href=\'([^\']+)').findall(kategoria)[0]
        title = re.compile(' title=\'([^\']+)').findall(kategoria)[0]
        add_video_item(sys.argv[0]+"?akcja=listuj&url="+urllib.quote_plus(href), {'title': '%s' % (title)} )
        xbmcplugin.endOfDirectory(plugin_handle)
    
    

