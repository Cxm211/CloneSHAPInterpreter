def unique(seq) :
	seen = set()
	for x in seq :
		if x not in seen :
			seen.add(x)
			yield x


def unique(x) :
	output = []
	y = {}
	for item in x :
		y [item] = ""
	for item in x :
		if item in y :
			output.append(item)
	return output

