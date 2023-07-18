def update_model(self, index) :
	parent = self.model.itemFromIndex(index)
	for text in ["children1", "children2", "children3"] :
		children = QtGui.QStandardItem("{}_{}".format(parent.text(), text))
		parent.appendRow(children)
	self.mytreeview.expand(index)


def update_model(self, index) :
	parent_item = self.model.itemFromIndex(index)
	if not parent_item.rowCount() :
		for child_name_entry in parent_text_fileobject :
			child_item = QtGui.QStandardItem(child_name_entry.strip())
			child_item.setData("this is a child", QtCore.Qt.ToolTipRole)
			parent_item.appendRow(child_item)

