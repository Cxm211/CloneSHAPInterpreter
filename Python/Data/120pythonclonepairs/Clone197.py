def compress(factors) :
	summands = collections.defaultdict(lambda : 0)
	for factor in factors :
		summands [factor] += 1
	return [(base, summands [base]) for base in sorted(summands)]


def compress(factors) :
	for (factor, copies) in itertools.groupby(factors) :
		power = len(list(copies))
		yield (factor, power)

