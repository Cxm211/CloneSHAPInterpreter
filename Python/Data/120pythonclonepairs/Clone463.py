def find_neighbors(pindex, triang) :
	neighbors = list()
	for simplex in triang.vertices :
		if pindex in simplex :
			neighbors.extend([simplex [i] for i in range(len(simplex)) if simplex [i] ! = pindex])
			'''
			this is a one liner for if a simplex contains the point we`re interested in,
			extend the neighbors list by appending all the *other* point indices in the simplex
			'''
	return list(set(neighbors))


def find_neighbors(tess, points) :
	neighbors = {}
	for point in range(points.shape [0]) :
		neighbors [point] = []
	for simplex in tess.simplices :
		neighbors [simplex [0]] += [simplex [1], simplex [2]]
		neighbors [simplex [1]] += [simplex [2], simplex [0]]
		neighbors [simplex [2]] += [simplex [0], simplex [1]]
	return neighbors

