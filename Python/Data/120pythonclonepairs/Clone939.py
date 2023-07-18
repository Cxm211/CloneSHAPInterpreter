def unique(x) :
	output = []
	y = {}
	for item in x :
		y [item] = ""
	for item in x :
		if item in y :
			output.append(item)
	return output


def unique(items) :
	found = set([])
	keep = []
	for item in items :
		if item not in found :
			found.add(item)
			keep.append(item)
	return keep

