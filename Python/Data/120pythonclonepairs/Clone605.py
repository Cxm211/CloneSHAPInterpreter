def __getitem__(self, item) :
	if isinstance(item, slice) :
		if item.step is None :
			return list(range(item.start, item.stop))
		return list(range(item.start, item.stop, item.step))


def __getitem__(self, item) :
	if isinstance(item, numbers.Integral) :
		return item
	if isinstance(item, slice) :
		return list(range(item.start or 0, item.stop or len(self), item.step or 1))
	else :
		raise TypeError('{cls} indices must be integers or slices, not {idx}'.format(
		cls = type(self).__name__,
		idx = type(item).__name__,
		))

