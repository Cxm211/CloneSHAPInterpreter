def is_continuous(seq) :
	non_null_indices = [i for i, obj in enumerate(seq) if obj is not None]
	for i, index in enumerate(non_null_indices [: - 1]) :
		if non_null_indices [i + 1] - index > 1 :
			return False
	return True


def is_continuous(seq) :
	try :
		first_none_pos = next(i for i, x in enumerate(seq) if x is not None)
		last_none_pos = - next(i for i, x in enumerate(reversed(seq)) if x is not None) or None
	except StopIteration :
		return False
	return None not in seq [first_none_pos : last_none_pos]

