def seq(start, end, step) :
	if step == 0 :
		raise ValueError("step must not be 0")
	sample_count = int(abs(end - start) / step)
	return itertools.islice(itertools.count(start, step), sample_count)


def seq(start, stop, step = 1) :
	n = int(round((stop - start) / float(step)))
	if n > 1 :
		return ([start + step * i for i in range(n + 1)])
	elif n == 1 :
		return ([start])
	else :
		return ([])

