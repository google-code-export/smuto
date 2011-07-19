import sys
import xbmcgui
import xbmcplugin


def showChannels():

    channels = list()
    channels.append({'title': 'Jedynka', 'logo': 'http://moje.polskieradio.pl/_img/kanaly/pr1.jpg', 'File': 'mms://stream.polskieradio.pl/program1_wma10'})
    channels.append({'title': 'Dwójka', 'logo': 'http://moje.polskieradio.pl/_img/kanaly/pr2.jpg', 'File': 'mms://stream.polskieradio.pl/program2_wma10'})
    channels.append({'title': 'Trójka', 'logo': 'http://moje.polskieradio.pl/_img/kanaly/pr3.jpg', 'File': 'mms://stream.polskieradio.pl/program3_wma10'})
    channels.append({'title': 'Czwórka', 'logo': 'http://moje.polskieradio.pl/_img/kanaly/pr4.jpg', 'File': 'mms://stream.polskieradio.pl/program4_wma10'})
    channels.append({'title': 'Koncerty w Trójce', 'logo': 'http://moje.polskieradio.pl/_img/kanaly/6.jpg', 'File': 'rtmp://stream85.polskieradio.pl/omniaaxe/k16.stream'})
    channels.append({'title': 'Przeboje Lata z Radiem', 'logo': 'http://moje.polskieradio.pl/_img/kanaly/14.jpg', 'File': 'rtmp://stream85.polskieradio.pl/omniaaxe/k24.stream'})
    channels.append({'title': 'Minimax', 'logo': 'http://moje.polskieradio.pl/_img/kanaly/24.jpg', 'File': 'rtmp://stream85.polskieradio.pl/omniaaxe/k34.stream'})
    channels.append({'title': 'Pod dachami Pary¿a', 'logo': 'http://moje.polskieradio.pl/_img/kanaly/23.jpg', 'File': 'rtmp://stream85.polskieradio.pl/omniaaxe/k33.stream'})
    channels.append({'title': 'Bajki samograjki', 'logo': 'http://moje.polskieradio.pl/_img/kanaly/27.jpg', 'File': 'rtmp://stream85.polskieradio.pl/omniaaxe/k37.stream'})

    for channel in channels:
        item = xbmcgui.ListItem(channel['title'], iconImage = channel['logo'], thumbnailImage = channel['logo'])
        item.setProperty('IsPlayable', 'true')
        item.setProperty("IsLive", "true")
        item.setInfo(type='Music', infoLabels = { 'title' : channel['title'] })
        #item.setInfo(type='Music', infoLabels = { 'artist' : channel['title'] })

        xbmcplugin.addDirectoryItem(HANDLE, channel['File'], item)

    xbmcplugin.endOfDirectory(HANDLE)

if __name__ == '__main__':
    HANDLE = int(sys.argv[1])
    showChannels()

