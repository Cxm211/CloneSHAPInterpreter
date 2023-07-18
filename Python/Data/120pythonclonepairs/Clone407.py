def ignore_until(the_list, match) :
	if match in the_list :
		index = the_list.index(match)
		return the_list [index :]
	else :
		return []


def ignore_until(the_list, match) :
	try :
		return the_list [the_list.index(match) :]
	except ValueError :
		return []

