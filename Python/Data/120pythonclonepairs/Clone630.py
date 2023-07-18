def merge_sort(sequence) :
	if len(sequence) < 2 :
		return sequence
	mid = len(sequence) / / 2
	left_sequence = merge_sort(sequence [: mid])
	right_sequence = merge_sort(sequence [mid :])
	return merge(left_sequence, right_sequence)


def merge_sort(x) :
	if len(x) < 2 : return x
	result, mid = [], int(len(x) / 2)
	y = merge_sort(x [: mid])
	z = merge_sort(x [mid :])
	while (len(y) > 0) and (len(z) > 0) :
		if y [0] > z [0] : result.append(z.pop(0))
		else : result.append(y.pop(0))
	result.extend(y + z)
	return result

