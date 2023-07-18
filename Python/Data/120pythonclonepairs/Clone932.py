def unique(l) :
	s = set(); n = 0
	for x in l :
		if x not in s : s.add(x); l [n] = x; n += 1
	del l [n :]


def unique(x) :
	output = []
	y = {}
	for item in x :
		y [item] = ""
	for item in x :
		if item in y :
			output.append(item)
	return output

