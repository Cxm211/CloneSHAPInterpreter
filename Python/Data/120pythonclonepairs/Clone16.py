def check_all_conditions() :
	for condition in all_conditions() :
		if condition :
			return condition
	return None


def check_all_conditions() :
	conditions = (check_size, check_color, check_tone, check_flavor)
	results_gen = dropwhile(lambda x : not x, imap(lambda check : check(), conditions))
	try :
		return results_gen.next()
	except StopIteration :
		return None

