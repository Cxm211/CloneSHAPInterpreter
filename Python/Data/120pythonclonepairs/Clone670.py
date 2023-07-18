def a(name) :
	global_variables = globals()
	try :
		name_of_passed_in_variable = [x for x in global_variables if id(global_variables [x]) == id(name)] [0]
	except Exception :
		name_of_passed_in_variable = "unknown"
	print name_of_passed_in_variable, name


def a(** kwargs) :
	valid_key = [k for k in kwargs.iterkeys() if k.startswith('bag') or k.startswith('basket')] [0]
	if valid.key.startswith('bag') :
		dist_list = ID ['bag']
	elif valid.key.startswith('basket') :
		dist_list = ID ['basket']
	else :
		raise Exception('a requires argument starting with `basket` or `bag`')

