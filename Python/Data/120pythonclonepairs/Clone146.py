def contains(small, big) :
	for i in xrange(len(big) - len(small) + 1) :
		for j in xrange(len(small)) :
			if big [i + j] ! = small [j] :
				break
		else :
			return i, i + len(small)
	return False


def contains(small, big) :
	for i in xrange(1 + len(big) - len(small)) :
		if small == big [i : i + len(small)] :
			return i, i + len(small) - 1
	return False

