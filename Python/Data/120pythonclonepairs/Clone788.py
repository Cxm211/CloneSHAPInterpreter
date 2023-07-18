def transpose(matrix) :
	li = []
	for i in range(len(matrix)) :
		inner_li = []
		for sets in matrix :
			inner_li.append(sets [i])
		li.append(inner_li)
	return li


def transpose(matrix) :
	n = 0
	li = []
	while n < (len(matrix)) :
		for sets in matrix :
			li.append(sets [0])
		n += 1
		print (len(matrix))
	return li

