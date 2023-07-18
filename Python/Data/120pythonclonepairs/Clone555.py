def chunks(iterable, n) :
	values = []
	for i, item in enumerate(iterable, 1) :
		values.append(item)
		if i % n == 0 :
			yield values
			values = []
	if values :
		yield values


def chunks(iterable, chunk_size) :
	i = 0;
	while i < len(iterable) :
		yield iterable [i : i + chunk_size]
		i += chunk_size

