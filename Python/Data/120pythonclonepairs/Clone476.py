def __init__(self, * args, ** kwargs) :
	wx.Frame.__init__(self, * args, ** kwargs)
	self.panel = wx.Panel(self)
	self.button = wx.Button(self.panel, label = "Test")
	self.sizer = wx.BoxSizer()
	self.sizer.Add(self.button)
	self.panel.SetSizerAndFit(self.sizer)
	self.Show()


def __init__(self, parent, * args, ** kwargs) :
	super(MainPanel, self).__init__(parent, * args, ** kwargs)
	"""Create and populate main sizer."""
	sizer = wx.BoxSizer(wx.VERTICAL)
	cmd_quit = wx.Button(self, id = wx.ID_EXIT)
	cmd_quit.Bind(wx.EVT_BUTTON, parent.on_quit_click)
	sizer.Add(cmd_quit)
	self.SetSizer(sizer)

