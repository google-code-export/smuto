import xbmcaddon, xbmc, xbmcgui

__settings__ = xbmcaddon.Addon(id='script.nowplaying')
__language__ = __settings__.getLocalizedString
__cwd__      = __settings__.getAddonInfo('path')
__icon__      = __settings__.getAddonInfo('icon')

class showInfo(xbmcgui.WindowXMLDialog):

#    def __init__(self, *args, **kwargs):
#        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def onInit(self):
        self.defineControls()
    def defineControls(self):
        self.action_cancel_dialog = (9, 10)
    def closeDialog(self):
        self.close()
    def onAction(self, action):
        if action in self.action_cancel_dialog:
            self.closeDialog()

if xbmc.Player().isPlayingAudio():
    w = showInfo("script-nowplaying.xml", __cwd__)
    w.doModal()
    del w
else:
    xbmc.executebuiltin("XBMC.Notification("+__language__(30000)+","+__language__(30001)+",5000,"+__icon__+")")


