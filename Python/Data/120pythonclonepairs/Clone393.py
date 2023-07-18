def permutations(string) :
	if len(string) == 1 :
		return string
	recursive_perms = []
	for c in string :
		for perm in permutations(string.replace(c, '', 1)) :
			revursive_perms.append(c + perm)
	return set(revursive_perms)


def permutations(string) :
	permutation_list = []
	if len(string) == 1 :
		return [string]
	else :
		for char in string :
			[permutation_list.append(char + a) for a in permutations(string.replace(char, ""))]
	return permutation_list

