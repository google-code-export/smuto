import os
import random

import xbmcgui
import imageDownloader
import xbmcaddon

import interia_scraper

_id = os.path.basename(os.getcwd())
Addon = xbmcaddon.Addon(_id)
#enable localization
getLS = Addon.getLocalizedString
starymiesiac = random.randint(06, 12)
nowymiesiac = random.randint(01, 10)


class GUI(xbmcgui.WindowXML):
    #Label Controls
    CONTROL_MAIN_IMAGE = 100
    CONTROL_USAGE_TEXT = 103
    #Label Actions
    ACTION_CONTEXT_MENU = [117]
    ACTION_MENU = [122]
    ACTION_PREVIOUS_MENU = [9]
    ACTION_SHOW_INFO = [11]
    ACTION_EXIT_SCRIPT = [10, 13]
    ACTION_DOWN = [4]
    ACTION_UP = [3]

    ACTIVESOURCE = 0
    
    SOURCES = list()
    SOURCES.append({'name': '990 pixeli: Najnowsze', 'object': 'tbp', 'url': 'http://www.990px.pl/'})
    SOURCES.append({'name': '990 pixeli: losowy %s 2010' % ( nowymiesiac), 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/2010/%s' % ( nowymiesiac)})
    SOURCES.append({'name': '990 pixeli: Historia', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/historia/'})
    SOURCES.append({'name': '990 pixeli: Kultura 1', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/kultura/'})
    SOURCES.append({'name': '990 pixeli: Kultura 2', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/kultura/page/2/'})
#    SOURCES.append({'name': '990 pixeli: Kultura 3', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/kultura/page/3/'})
    SOURCES.append({'name': '990 pixeli: Lifestyle 1', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/lifestyle/'})
    SOURCES.append({'name': '990 pixeli: Lifestyle 2', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/lifestyle/page/2/'})
    SOURCES.append({'name': '990 pixeli: Lifestyle 3', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/lifestyle/page/3/'})
    SOURCES.append({'name': '990 pixeli: Lifestyle 4', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/lifestyle/page/4/'})
    SOURCES.append({'name': '990 pixeli: Ludzie', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/ludzie/'})
    SOURCES.append({'name': '990 pixeli: Mundial', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/mundial/'})
    SOURCES.append({'name': '990 pixeli: Natura', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/natura/'})
    SOURCES.append({'name': '990 pixeli: Owce', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/owce/'})
    SOURCES.append({'name': '990 pixeli: Polityka', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/polityka/'})
    SOURCES.append({'name': '990 pixeli: Sport 1', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/sport/'})
    SOURCES.append({'name': '990 pixeli: Sport 2', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/sport/page/2/'})
    SOURCES.append({'name': '990 pixeli: Technologia', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/technologia/'})
    SOURCES.append({'name': '990 pixeli: Vancouver', 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/category/vancouver/'})
    SOURCES.append({'name': '990 pixeli: losowy %s 2009' % ( starymiesiac), 'object': 'tbp', 'url': 'http://www.990px.pl/index.php/2009/%s' % ( starymiesiac)})


    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)
        self.tbp = interia_scraper.TBP()

    def onInit(self):
        self.getControl(102).setLabel(getLS(32001)) #fixme
        self.showAlbums()

    def onFocus(self, controlId):
        pass

    def onAction(self, action):
        if action in self.ACTION_SHOW_INFO:
            self.toggleInfo()
        elif action in self.ACTION_CONTEXT_MENU:
            self.download()
        elif action in self.ACTION_PREVIOUS_MENU:
            # exit the script
            if self.getProperty('type') == 'album':
                self.close()
            # return to previous album
            elif self.getProperty('type') == 'photo':
                self.showAlbums()
        elif action in self.ACTION_EXIT_SCRIPT:
            self.close()
        elif action in self.ACTION_DOWN and self.getProperty('type') == 'album':
            if len(self.SOURCES) > self.ACTIVESOURCE + 1:
                self.ACTIVESOURCE += 1
            else:
                self.ACTIVESOURCE = 0
            self.showAlbums()
        elif action in self.ACTION_UP and self.getProperty('type') == 'album':
            if self.ACTIVESOURCE == 0:
                self.ACTIVESOURCE = len(self.SOURCES) - 1
            else:
                self.ACTIVESOURCE -= 1
            self.showAlbums()

    def onClick(self, controlId):
        if controlId == self.CONTROL_MAIN_IMAGE:
            if self.getProperty('type') == 'album':
                self.showPhotos()
            elif self.getProperty('type') == 'photo':
                self.toggleInfo()

    def getProperty(self, property, controlId=CONTROL_MAIN_IMAGE):
        """Returns a property of the selected item"""
        return self.getControl(controlId).getSelectedItem().getProperty(property)

    def toggleInfo(self):
        selectedControl = self.getControl(self.CONTROL_MAIN_IMAGE)
        if self.getProperty('showInfo') == 'false':
            for i in range(selectedControl.size()):
                selectedControl.getListItem(i).setProperty('showInfo', 'true')
                self.getControl(self.CONTROL_USAGE_TEXT).setVisible(True)
        else:
            for i in range(selectedControl.size()):
                selectedControl.getListItem(i).setProperty('showInfo', 'false')
                self.getControl(self.CONTROL_USAGE_TEXT).setVisible(False)

    def download(self):
        #get writable directory
        downloadPath = xbmcgui.Dialog().browse(3, ' '.join([getLS(32020), getLS(32022)]), 'pictures')
        if downloadPath:
            if self.getProperty('type') == 'photo':
                photos = [{'pic':self.getProperty('pic'), 'title': ''}] #url needs to be passed as a dict in a list.
                imageDownloader.Download(photos, downloadPath) 
            elif self.getProperty('type') == 'album':
                pDialog = xbmcgui.DialogProgress() #show useless dialog so user knows something is happening.
                pDialog.create(self.SOURCES[self.ACTIVESOURCE]['name'])
                link = self.getProperty('link')
                pDialog.update(50)
                if self.SOURCES[self.ACTIVESOURCE]['object'] == 'tbp':
                    self.tbp.getPhotos(link) # Get a list of photos from the link.
                    photos = self.tbp.photos
                else:
                    photos = {'title': '', 'pic': '', 'description': ''}
                pDialog.update(100)
                pDialog.close()
                imageDownloader.Download(photos, downloadPath)

    def showPhotos(self): #the order is significant!
        self.getControl(self.CONTROL_USAGE_TEXT).setText('\n'.join([getLS(32030), getLS(32031), getLS(32032)]))
        link = self.getProperty('link')
        self.getControl(self.CONTROL_MAIN_IMAGE).reset() #Clear the old list of albums.
        if self.SOURCES[self.ACTIVESOURCE]['object'] == 'tbp':
            self.tbp.getPhotos(link) # Get a list of photos from the link.
            photos = self.tbp.photos
        else:
            photos = [{'title': '', 'pic': '', 'description': ''}]
        self.showItems(photos, 'photo')

    def showAlbums(self):
        self.getControl(self.CONTROL_USAGE_TEXT).setText('\n'.join([getLS(32040), getLS(32041), getLS(32042)]))
        self.getControl(self.CONTROL_MAIN_IMAGE).reset() #This is necessary when returning from photos.
        if self.SOURCES[self.ACTIVESOURCE]['object'] == 'tbp':
            self.tbp.getAlbums(self.SOURCES[self.ACTIVESOURCE]['url'])
            albums = self.tbp.albums
        else:
            albums = [{'title': '', 'pic': '', 'description': '', 'link': ''}]
        self.showItems(albums, 'album')

    def showItems(self, itemSet, type):
        total = len(itemSet)
        for i, item in enumerate(itemSet):
            item['showInfo'] = 'true'
            item['type'] = type
            item['title'] = self.SOURCES[self.ACTIVESOURCE]['name'] + '\n' + item['title'] + ' (%s/%s)' % (i+1, total)
            self.addListItem(self.CONTROL_MAIN_IMAGE, item)

    def addListItem(self, controlId, properties):
        #print properties
        li = xbmcgui.ListItem(label=properties['title'], label2=properties['description'], iconImage=properties['pic'])
        for p in properties.keys():
            li.setProperty(p, properties[p])
        self.getControl(controlId).addItem(li)
