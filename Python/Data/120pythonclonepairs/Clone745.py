def __init__(self, parent) :
	wx.Panel.__init__(self, parent)
	self.figure = mplFigure(figsize = (9, 6))
	self.ax = self.figure.add_subplot(111)
	self.ax.plot([1, 2, 3, 4], [2, 3, 5, 8], marker = "o", markersize = 20, picker = 10, linestyle = "None")
	self.canvas = mplCanvas(self, - 1, self.figure)
	self.figure.canvas.mpl_connect('pick_event', self.onClick)
	self.canvas.Bind(wx.EVT_KEY_DOWN, self._on_key_down)
	self.canvas.Bind(wx.EVT_KEY_UP, self._on_key_up)
	self.states = {"cmd" : False, "ctrl" : False, "shift" : False}


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

