# -*- coding: utf-8 -*-
import xbmcplugin, xbmcaddon, xbmcgui, xbmc
import sys, os, stat, re
import urllib

scriptID = sys.modules[ "__main__" ].scriptID

class Settings:
  def __init__(self):
    addon = xbmcaddon.Addon(scriptID)  
    params = self.getParams()
    self.numOfNewestTrailers = self.getParam(params, 'numOfNewestTrailers')
    self.numOfRandomTrailers = self.getParam(params, "numOfRandomTrailers")

  def getParam(self, params, name):
    try:
      result = params[name]
      result = urllib.unquote_plus(result)
      return result
    except:
      return None

  def getIntParam (self, params, name):
    try:
      param = self.getParam(params, name)
      return int(param)
    except:
      return None
    
  def getBoolParam (self, params, name):
    try:
      param = self.getParam(params,name)
      return 'True' == param
    except:
      return None
    
  def getParams(self):
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

  def showSettings(self):
    xbmcaddon.Addon(scriptID).openSettings(sys.argv[0])