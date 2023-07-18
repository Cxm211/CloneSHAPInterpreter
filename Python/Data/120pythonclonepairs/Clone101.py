def num_input(prompt, error) :
	while True :
		result = raw_input(prompt)
		for candidate in (int, float) :
			try : return candidate(result)
			except ValueError : pass
		print error


def num_input(s) :
	while True :
		try :
			return decimal.Decimal(raw_input(s))
		except decimal.InvalidOperation, e :
			print e.message

