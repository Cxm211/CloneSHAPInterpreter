def __init__(self) :
	wx.Frame.__init__(self, None, - 1, "matplotlib pick_event problem")
	self.plotarea = PlotPanel(self)
	self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
	self.mainSizer.Add(self.plotarea, 1, wx.EXPAND)
	self.SetSizer(self.mainSizer)
	self.mainSizer.Fit(self)


def __init__(self, parent) :
	pre = wx.PreDialog()
	pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
	pre.Create(parent, - 1, "sample dialog", size = (200, 100), style = wx.CAPTION | wx.RESIZE_BORDER)
	self.PostCreate(pre)
	self.parent = parent
	self.Bind(wx.EVT_KEY_DOWN, self.parent._on_key_down)
	self.Bind(wx.EVT_KEY_UP, self.parent._on_key_up)
	btn = wx.Button(self, - 1, "OK")
	btn.Bind(wx.EVT_BUTTON, self._OnClick)

