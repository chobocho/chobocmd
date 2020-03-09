import wx

class CmdMenu():
    def __init__(self, parent):
        self.parent = parent
        self._addMenubar()

    def _addMenubar(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        viewItemID = wx.NewId()
        viewItem = fileMenu.Append(viewItemID, 'Result view', 'Result view')
        self.parent.Bind(wx.EVT_MENU, self.parent.OnShowResultView, viewItem)

        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit App')
        self.parent.Bind(wx.EVT_MENU, self.parent.OnQuit, fileItem)
        menubar.Append(fileMenu, '&File')

        helpMenu = wx.Menu()
        aboutItemId = wx.NewId()
        aboutItem = helpMenu.Append(aboutItemId, 'About', 'About')
        self.parent.Bind(wx.EVT_MENU, self.parent.OnAbout, aboutItem)
        menubar.Append(helpMenu, '&Help')

        self.parent.SetMenuBar(menubar)
