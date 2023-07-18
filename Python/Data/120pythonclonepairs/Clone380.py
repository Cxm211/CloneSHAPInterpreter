def foo(bar = None, i = 10) :
	if bar is None :
		bar = set()
	if i == 0 :
		return bar
	bar |= set(random.randint(1, 1000) for i in xrange(10))
	return foo(bar, i - 1)


def foo() :
	acc = Accumulator()
	acc.value = 0
	def bar(n) :
		if (n > 0) : bar(n - 1)
		acc.value = acc.value + 1
	bar(5)
	return acc.value

