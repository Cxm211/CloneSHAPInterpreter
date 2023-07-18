def breakdown(a) :
	y = []
	q = len(a)
	while q > 0 :
		y += [list(a)]
		a.pop()
		q -= 1
	return y


def breakdown(li) :
	result = []
	for i in range(len(li) - 1, - 1, - 1) :
		result.append(li [: i + 1])
	return result

