def my_function(a) :
	a = iter(a)
	while True :
		yield 10 * next(a)
		yield next(a)
		yield "foo" + next(a)


def my_function(lst) :
	items = (lst [i : i + 3] for i in xrange(0, len(lst), 3))
	for group in items :
		yield group [0] * 10
		yield group [1]
		yield 'foo' + group [2]

