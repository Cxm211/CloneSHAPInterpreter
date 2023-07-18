def almostIncreasingSequence(sequence) :
	t = 0
	for i in range(len(sequence)) :
		temp = sequence.copy()
		del temp [i]
		if temp == sorted(temp) and not (any(i == j for i, j in zip(sorted(temp), sorted(temp) [1 :]))) :
			t += 1
	return t > 0


def almostIncreasingSequence(sequence) :
	j = first_bad_pair(sequence, - 1)
	if j == - 1 :
		return True
	if first_bad_pair(sequence, j) == - 1 :
		return True
	if first_bad_pair(sequence, j + 1) == - 1 :
		return True
	return False

