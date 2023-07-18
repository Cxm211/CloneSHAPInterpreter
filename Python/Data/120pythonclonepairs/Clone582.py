def reverse(s) :
	i = len(s) - 1
	sNew = ''
	while i > = 0 :
		sNew = sNew + str(s [i])
		i = i - 1
	return sNew


def reverse(text) :
	reversed_text = ""
	for n in range(len(text)) :
		reversed_text += text [- 1 - n]
	return reversed_text

