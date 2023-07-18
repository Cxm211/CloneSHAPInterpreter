def a(name) :
	global_variables = globals()
	try :
		name_of_passed_in_variable = [x for x in global_variables if id(global_variables [x]) == id(name)] [0]
	except Exception :
		name_of_passed_in_variable = "unknown"
	print name_of_passed_in_variable, name


def a(** kwargs) :
	if len(kwargs) ! = 1 :
		raise ValueError("only pass a single keyword arg starting with 'bag' or 'basket'")
	name, value = list(kwargs.items()) [0]
	if name.startswith('bag') :
		dist_list = ID ['bag']
	else :
		dist_list = ID ['basket']
	dist_list.append(value)

