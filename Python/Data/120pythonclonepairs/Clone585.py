def reverse(s) :
	t = - 1
	s2 = ''
	while abs(t) < len(s) + 1 :
		s2 = s2 + s [t]
		t = t - 1
	return s2


def reverse(s) :
	rev = [_t for _t in s]
	t = ''
	while len(rev) ! = 0 :
		t += rev.pop()
	return t

