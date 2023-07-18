def touch_value(self, stack, frame) :
	assert self.pushes == 0
	for i in range(self.pops) :
		stack.pop()


def touch_value(self, stack, frame) :
	name = self.get_arg()
	if name not in frame :
		raise UnknownSymbol("Does not know symbol {}".format(name))
	stack.append(frame [name])

