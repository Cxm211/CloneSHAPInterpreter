def num_subsequences(seq, sub) :
	if not sub :
		return 1
	elif not seq :
		return 0
	result = num_subsequences(seq [1 :], sub)
	if seq [0] == sub [0] :
		result += num_subsequences(seq [1 :], sub [1 :])
	return result


def num_subsequences(seq, sub) :
	m, n = len(seq), len(sub)
	@ lru_cache(maxsize = None)
	def count(i, j) :
		if j == n :
			return 1
		elif i == m :
			return 0
		return count(i + 1, j) + (count(i + 1, j + 1) if seq [i] == sub [j] else 0)
	return count(0, 0)

