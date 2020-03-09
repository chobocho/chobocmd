import wx

from ui.cmdpanel import *
from ui.cmdmenu import *

WINDOW_SIZE = 640

class CommanderFrame(wx.Frame):
    def __init__(self, *args, version, **kw):
        super(CommanderFrame, self).__init__(*args, **kw)
    
        self.version = version
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.cmdPanel = CommanderPanel(self, parent_=self)
        self.sizer.Add(self.cmdPanel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self._addMenubar()

    def _addMenubar(self):
        self.menu = CmdMenu(self)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        title = 'About'
        msg = self.version+'\nhttp://chobocho.com'
        self.OnShowMessasgeBox(title, msg)

    def OnShowMessasgeBox(self, title, msg):
        wx.MessageBox(msg, title, wx.OK | wx.ICON_INFORMATION)

    def OnShowResultView(self, event):
        self.cmdPanel.toggleResultViewShow()
        self.OnUpdateSize()

    def OnUpdateSize(self):
        if self.cmdPanel.isResultViewShow():
            self.SetSize(WINDOW_SIZE, 220)
        else:
            self.SetSize(WINDOW_SIZE, 100)
