def checkio(data) :
	for index in range(len(data) - 1, - 1, - 1) :
		if data.count(data [index]) == 1 :
			del data [index]
	return data


def checkio(data) :
	lis = []
	for i in data :
		if data.count(i) > 1 :
			lis.append(i)
	print (lis)

