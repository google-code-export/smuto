import os
import sys

# Script constants
__scriptname__ = '990 pixeli'
__author__ = 'sphere, rwparris2, smuto'
__version__ = '0.0.1'

print '[SCRIPT][%s] version %s initialized!' % (__scriptname__, __version__)

if (__name__ == '__main__'):
    import resources.lib.gui as gui
    ui = gui.GUI( 'main.xml', os.getcwd(), 'default' )
    ui.doModal()
    del ui
    sys.modules.clear()
