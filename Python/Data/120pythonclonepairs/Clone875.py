def sublist(a, b) :
	seq = iter(b)
	try :
		for x in a :
			while next(seq) ! = x : pass
		else :
			return True
	except StopIteration :
		pass
	return False


def sublist(a, b) :
	if not a :
		return True
	for k in range(len(b)) :
		if a [0] == b [k] :
			return sublist(a [1 :], b [k + 1 :])
	return False

