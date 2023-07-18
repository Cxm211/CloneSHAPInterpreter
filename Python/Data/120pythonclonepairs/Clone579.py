def rev(test) :
	test = list(test)
	i = len(test) - 1
	result = []
	print test
	while i > = 0 :
		result.append(test.pop(i))
		i -= 1
	return "".join(result)


def rev(s) :
	l = len(s)
	for i, j in zip(range(l - 1, 0, - 1), range(l / / 2)) :
		s [i], s [j] = s [j], s [i]
	return s

