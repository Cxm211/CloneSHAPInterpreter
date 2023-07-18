def backspace(self) :
	self.current = self.current [0 : len(self.current) - 1]
	if self.current == "" :
		self.new_num = True
		self.current = "0"
	self.dsiplay(self.current)


def backspace(self) :
	if re.match(r'\d$', self.current) :
		self.display(0)
		self.new_num = True
	else :
		self.current = self.current [: - 1]
		self.display(self.current)

