def length_of_string(mystring) :
	if type(mystring) is int :
		return "invalid entry"
	else :
		return len(mystring)


def length_of_string(mystring) :
	try :
		int(mystring)
		return "invalid entry"
	except ValueError :
		return len(mystring)

