def deep_reverse(p) :
	if p == [] :
		return p
	if not is_list(p [0]) :
		return deep_reverse(p [1 :]) + [p [0]]
	else :
		return deep_reverse(p [1 :]) + [deep_reverse(p [0])]


def deep_reverse(a) :
	a.reverse()
	for i in a :
		if is_list(i) :
			deep_reverse(i)
			print a

