def num_input(prompt, error) :
	while True :
		result = raw_input(prompt)
		for candidate in (int, float) :
			try : return candidate(result)
			except ValueError : pass
		print error


def num_input(prompt, error) :
	s = raw_input(prompt)
	for t in (int, float, complex) :
		try : return t(s)
		except ValueError : pass
	print error
	return num_input(prompt, error)

