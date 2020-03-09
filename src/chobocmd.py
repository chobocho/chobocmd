import wx
from ui.cmdframe import *

SW_TITLE = "ChoboCmd V0.1.TC1"
WINDOW_SIZE = 640

def main(): 
    app = wx.App()
    frm = CommanderFrame(None, version=SW_TITLE, title=SW_TITLE,
                         #style=(wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)),
                         size=(WINDOW_SIZE,100))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()