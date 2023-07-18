def reverse(s) :
	i = len(s) - 1
	sNew = ''
	while i > = 0 :
		sNew = sNew + str(s [i])
		i = i - 1
	return sNew


def reverse(text) :
	lst = []
	count = 1
	for i in range(0, len(text)) :
		lst.append(text [len(text) - count])
		count += 1
	lst = ''.join(lst)
	return lst

