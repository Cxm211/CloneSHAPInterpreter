def reverseParentheses(s) :
	if '(' in s :
		posopen = s.find('(')
		s = s [: posopen] + reverseParentheses(s [posopen + 1 :])
		posclose = s.find(')', posopen + 1)
		s = s [: posopen] + s [posopen : posclose] [: : - 1] + s [posclose + 1 :]
	return s


def reverseParentheses(s) :
	if s.find('(') == - 1 :
		return s
	if s.find('(') < s.find(')') :
		beg, end = s.find('('), s.rfind(')')
	else :
		beg, end = s.find(')'), s.rfind('(')
	return s [: beg] + reverseParentheses(s [beg + 1 : end] [: : - 1]) + s [end + 1 :]

