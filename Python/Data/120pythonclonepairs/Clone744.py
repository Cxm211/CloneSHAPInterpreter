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


def __init__(self) :
	wx.Frame.__init__(self, None, - 1, "matplotlib pick_event problem")
	self.plotarea = PlotPanel(self)
	self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
	self.mainSizer.Add(self.plotarea, 1, wx.EXPAND)
	self.SetSizer(self.mainSizer)
	self.mainSizer.Fit(self)

