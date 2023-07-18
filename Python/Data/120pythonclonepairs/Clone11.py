def shift_n_letters(letter, n) :
	result = ord(letter) + n
	while result > ord('z') :
		result -= 26
	while result < ord('a') :
		result += 26
	return chr(result)


def shift_n_letters(letter, n) :
	n_ = n % 26
	result = chr(ord(letter) + n_)
	if ord(result) > 122 :
		result = chr(ord(result) - 26)
	return result

