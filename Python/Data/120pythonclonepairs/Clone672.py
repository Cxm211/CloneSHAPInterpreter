def increase_by_one(d) :
	for key in d :
		if type(d [key]) == dict :
			d [key] = increase_by_one(d [key])
		else :
			d [key] += 1
	return d


def increase_by_one(d) :
	for key in d :
		try :
			d [key] += 1
		except :
			increase_by_one(d [key])
	return d

