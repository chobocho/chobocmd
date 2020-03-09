import wx

WINDOW_SIZE = 640


class CommanderPanel(wx.Panel):
    def __init__(self, *args, parent_, **kw):
        super(CommanderPanel, self).__init__(*args, **kw)
        self.parent = parent_
        self._initButton()

    def _initButton(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.resultText = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, size=(WINDOW_SIZE,120))
        self.resultText.SetValue("")
        self.resultText.Hide()
        sizer.Add(self.resultText, 0, wx.ALIGN_CENTRE, 1)

        btnBox = wx.BoxSizer(wx.HORIZONTAL)
        self.cmdText = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, size=(WINDOW_SIZE-60,30))
        self.cmdText.SetValue("")
        btnBox.Add(self.cmdText, 1, wx.EXPAND, 1)
        self.cmdText.Bind(wx.EVT_TEXT_ENTER, self.OnRunCmdBtn)

        clearBtnId = wx.NewId()
        self.clearBtn = wx.Button(self, clearBtnId, "Clear", size=(50,30))
        self.clearBtn.Bind(wx.EVT_BUTTON, self.OnClearBtn)
        btnBox.Add(self.clearBtn, 0, wx.ALIGN_CENTRE, 1)

        sizer.Add(btnBox, 0, wx.EXPAND, 1)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)

    def OnClearBtn(self, event):
        self.cmdText.SetValue("")

    def OnRunCmdBtn(self, event):
        pass

    def isResultViewShow(self):
        return self.resultText.IsShown()

    def toggleResultViewShow(self):
        if self.resultText.IsShown():
            self.resultText.Hide()
        else:
            self.resultText.Show()