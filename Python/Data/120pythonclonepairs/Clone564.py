def brute_force(length, check_callback, guess = "") :
	if check_callback(guess) :
		return guess
	elif len(guess) == length :
		return None
	for char in chars :
		retval = brute_force(length, check_callback, guess = guess + char)
		if retval is not None :
			return retval
	return None


def brute_force() :
	for length in range(min_length, max_length + 1) :
		for p in product(chars, repeat = length) :
			guess = ''.join(p)
			if guess == password :
				return guess

