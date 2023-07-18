def linspace(start, stop, n) :
	if n == 1 :
		yield stop
		return
	h = (stop - start) / (n - 1)
	for i in range(n) :
		yield start + h * i


def linspace(a, b, n = 100) :
	if n < 2 :
		return b
	diff = (float(b) - a) / (n - 1)
	return [diff * i + a for i in range(n)]

