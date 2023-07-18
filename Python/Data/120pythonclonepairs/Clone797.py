def count(list1) :
	x = 0
	total = 0
	while x < len(list1) :
		total += list [x]
		print total
		x = x + 1
	return total


def count(list1) :
	total = 0
	old = 0
	for position, x in enumerate(list1) :
		total = x + old
		old = x
		print total
	return

