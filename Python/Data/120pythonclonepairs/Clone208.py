def is_sorted(stuff) :
	for i in range(1, len(stuff)) :
		if stuff [i - 1] > stuff [i] :
			return False
	return True


def is_sorted(stuff) :
	for index, item in enumerate(stuff) :
		try :
			if item > stuff [index + 1] :
				return False
		except IndexError :
			return True

