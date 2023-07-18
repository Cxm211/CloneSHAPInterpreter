def iter_n(self) :
	self.a, self.b = self.b, self.a + self.b
	if self.a > 10 :
		raise StopIteration();
	return self.a


def iter_n(self) :
	self.a, self.b = self.b, self.a + self.b
	if self.a > 10 :
		raise StopIteration();
	return self.a
	if sys.version_info [0] == 2 :
		next = iter_n
	else :
		__next__ = iter_n
	del iter_n

