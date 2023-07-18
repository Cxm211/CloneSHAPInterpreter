def sameSet(list1, list2) :
	if contained(list1, list2) and contained(list2, list1) :
		print ("the same!!")
	else :
		print ("not the same")


def sameSet(a, b) :
	l1, l2 = (a, b) if len(a) > len(b) else (b, a)
	for val in l1 :
		if val not in l2 :
			return False
	return True

