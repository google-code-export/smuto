# -*- coding: utf-8 -*-
import xbmcaddon

import sys, cgi, re
import simplejson
import urllib2

import xbmcgui
import xbmcplugin

import time

pluginHandle = int(sys.argv[1])
pluginQuery = sys.argv[2]
polskieradio_url = 'http://moje.polskieradio.pl'
idKey = '20439fdf-be66-4852-9ded-1476873cfa22'
format = 'json'

__settings__ = xbmcaddon.Addon(id='plugin.audio.mojepolskieradio.pl')
__language__ = __settings__.getLocalizedString
__cwd__      = __settings__.getAddonInfo('path')

CHANNELS_URL = polskieradio_url + '/api/?key=' + idKey + '&output=' + format

def showChannels():
    u = urllib2.urlopen(CHANNELS_URL)
    data = u.read()
    json = simplejson.loads(data)
    u.close()
    channels = json['channel']
    for channel in channels:
        xbmcplugin.setContent(pluginHandle, 'albums')
        item = xbmcgui.ListItem(channel['title'], iconImage = channel['image'], thumbnailImage = channel['image'])
        item.setProperty('IsPlayable', 'true')
        item.setProperty("IsLive", "true")
        item.setProperty('Album_Description', channel['description'].replace('\n',' '))
        item.setInfo( type="Music",  infoLabels = {
                'title' : 'PolskieRadio' ,
                'artist' : 'moje.polskieradio.pl' ,
                'year': 2012 ,
                'genre': channel['category'] ,
                'album' : channel['title'] ,
                'comment' : channel['description']
        })
        streams = channel["AlternateStationsStreams"]
        xbmc_streams = []
        for stream in streams:
            if stream['name'] == "mp3":
                link = stream['link']
                xbmc_streams.append(link)
            if  stream['name'] == "RTMP":
                link = stream['link']
                xbmc_streams.append(link)
        if __settings__.getSetting('stream') == "mp3":
            data_url = xbmc_streams[0]
        else:
            data_url = xbmc_streams[-1]

        runner = ',%d,?mode=info&gsid=%d&station=%s&data_url=%s' % (pluginHandle, channel['gsid'], channel['title'], data_url )
        contextMenu = [(__language__(30001),'XBMC.RunScript(special://home/addons/plugin.audio.mojepolskieradio.pl/addon.py'+runner+')')]
        item.addContextMenuItems(contextMenu)

        xbmcplugin.addDirectoryItem(pluginHandle, data_url, item)

    xbmcplugin.endOfDirectory(pluginHandle)

class showInfo(xbmcgui.WindowXMLDialog):
    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)
        self.gsid = kwargs['gsid']
        self.infostation = kwargs['station']
        self.data_url = kwargs['data_url']
        url = 'http://moje.polskieradio.pl/getPlaylist.aspx?stationId=%s' % (self.gsid)
        print url
        u = urllib2.urlopen(url)
        data = u.read()
        self.assets = simplejson.loads(data)
        u.close()
        if not self.assets:
            pass   
        else:
            for item in self.assets:
                start = item['Dates']['AirStarttime'].replace('/Date(','').replace(')/','')
                start_time = float(start)/1000
                stop = item['Dates']['AirStoptime'].replace('/Date(','').replace(')/','')
                stop_time = float(stop)/1000
                Time = time.time()
    
                if start_time < Time and Time < stop_time :  
                    self.infotitle = item['Info'].get('Title','')
                    self.infoalbum = item['Info'].get('Album','')
                    self.infoartist = item['Info'].get('Artist','')
                    self.infonote = self.htmlToText(item['Info'].get('Note',''))
                    self.infophoto = item['Info'].get('Photo','')
                    self.infostart_time = time.localtime(start_time)
                    self.infostop_time = time.localtime(stop_time)


    def htmlToText(self,html):
        html = re.sub('<.*?>','',html)
        return html	.replace("&lt;", "<")\
                    .replace("&gt;", ">")\
                    .replace("&amp;", "&")\
                    .replace("&quot;",'"')\
                    .replace("&nbsp;",'')\
                    .replace("&apos;","'")

    def onInit(self):
        self.defineControls()
        self.showDialog()

    def defineControls(self):
        #actions
        self.action_cancel_dialog = (9, 10)
        self.control_infostation_id         = 11        
        self.control_infotitle_id           = 13
        self.control_infoalbum_id           = 14
        self.control_infoartist_id          = 15        
        self.control_infonote_id            = 16
        self.control_infophoto_id           = 17
        self.control_flipyphoto_id          = 12
        self.control_play_button_id         = 18
        self.control_cancel_button_id       = 19
        self.control_start_time_id          = 20
        self.control_stop_time_id           = 21
        #controls
        self.infostation_value       = self.getControl(self.control_infostation_id)
        self.infotitle_value       = self.getControl(self.control_infotitle_id)
        self.infoalbum_value       = self.getControl(self.control_infoalbum_id)
        self.infoartist_value       = self.getControl(self.control_infoartist_id)
        self.infonote_value       = self.getControl(self.control_infonote_id)
        self.infophoto_value       = self.getControl(self.control_infophoto_id)
        self.flipyphoto_value       = self.getControl(self.control_flipyphoto_id)
        self.play_button          = self.getControl(self.control_play_button_id)
        self.cancel_button      = self.getControl(self.control_cancel_button_id)
        self.infostart_time_value          = self.getControl(self.control_start_time_id)
        self.infostop_time_value      = self.getControl(self.control_stop_time_id)

    def showDialog(self):
        self.infostation_value.setLabel(self.infostation)
        self.infotitle_value.addLabel(self.infotitle)
        self.infoalbum_value.addLabel(self.infoalbum)
        self.infoartist_value.addLabel(self.infoartist)
        self.infonote_value.setText(self.infonote)
        self.infoimage = 'http://moje.polskieradio.pl/_files/'+self.infophoto.replace('.jpg','_big.jpg')
        self.infophoto_value.setImage(self.infoimage)
        self.flipyphoto_value.setImage(self.infoimage)
        self.infostart_time_value.addLabel(time.strftime("%H:%M", self.infostart_time))
        self.infostop_time_value.addLabel(time.strftime("%H:%M", self.infostop_time))



    def closeDialog(self):
        self.close()
    def onClick(self, controlId):
        #play
        if controlId == self.control_play_button_id:
            xbmc.Player().play(self.data_url) 
            self.closeDialog()
        #cancel dialog
        elif controlId == self.control_cancel_button_id:
            self.closeDialog()
    def onAction(self, action):
        if action in self.action_cancel_dialog:
            self.closeDialog()


query = cgi.parse_qs(pluginQuery[1:])

for key, value in query.items():
    query[key] = value[0]
query['mode'] = query.get('mode', '')    
if query['mode'] == 'info':
    w = showInfo("script-PolskieRadio-Info.xml", __cwd__, "default", gsid = query['gsid'], station = query['station'], data_url = query['data_url'])
    w.doModal()
    del w
else:
    showChannels()

