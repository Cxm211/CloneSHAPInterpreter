def get_leaves(node) :
	for child in getchildren(node) :
		if leafnode(child) :
			for each in get_leaves(child) :
				yield each
		else :
			yield process_leaf(child)


def get_leaves(node, list_of_leaves = None) :
	list_of_leaves = [] if list_of_leaves is None else list_of_leaves
	kids = getchildren(node)
	for i in kids :
		if leafnode(i) :
			get_leaves(i, list_of_leaves)
		else :
			a = process_leaf(i)
			list_of_leaves.append(a)

