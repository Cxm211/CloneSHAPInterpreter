def reverse(string) :
	tmp = ""
	for i in range(1, len(string) + 1) :
		tmp += string [len(string) - i]
	return tmp


def reverse(s) :
	t = - 1
	s2 = ''
	while abs(t) < len(s) + 1 :
		s2 = s2 + s [t]
		t = t - 1
	return s2

