def now_next(sequence, n = 2) :
	iterators = itertools.tee(iter(sequence), n)
	for i, iterator in enumerate(iterators) :
		for j in range(i) :
			iterator.next()
	return itertools.izip(* iterators)


def now_next(gen, n = 2) :
	gens = tee(gen, n)
	gens = list(gens)
	for i, gen in enumerate(gens) :
		gens [i] = islice(gens [i], i, None)
	return izip(* gens)

