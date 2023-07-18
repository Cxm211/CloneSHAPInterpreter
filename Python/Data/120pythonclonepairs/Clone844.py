def f(n) :
	if n == 0 :
		return 0
	if n == 1 :
		return 1
	else :
		return 0.5 * (f(n - 1) + f(n - 2))


def f(n) :
	def aux(n, acc, a, b) :
		if n == 0 :
			return acc + [a]
		else :
			return aux(n - 1, acc + [a], b, 0.5 * (a + b))
	return aux(n, [], 0, 1)

