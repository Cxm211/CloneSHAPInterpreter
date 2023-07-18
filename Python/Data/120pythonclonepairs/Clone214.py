def checkio(data) :
	elements = []
	duplicates = []
	for i in data :
		if i not in elements :
			elements.append(i)
		else :
			if i not in duplicates :
				duplicates.append(i)
	return duplicates


def checkio(data) :
	lis = []
	for i in data :
		if data.count(i) > 1 :
			lis.append(i)
	print (lis)

