def foo(thing = None, thing_seq = None) :
	if thing_seq is not None :
		for _thing in thing_seq :
			foo(thing = _thing)
	if thing is not None :
		print "did foo with", thing


def foo(x) :
	if not isinstance(x, list) :
		x = [x]
	for y in x :
		do_something(y)

