def find_nth(haystack, needle, n = 1) :
	if (hasattr(needle, 'finditer')) :
		matches = needle.finditer(haystack)
	else :
		matches = re.finditer(re.escape(needle), haystack)
	start_here = itertools.dropwhile(lambda x : x [0] < n, enumerate(matches, 1))
	try :
		return next(start_here) [1].start()
	except StopIteration :
		return - 1


def find_nth(s, substr, n) :
	i = 0
	while n > = 0 :
		n -= 1
		i = s.find(substr, i + 1)
	return i

