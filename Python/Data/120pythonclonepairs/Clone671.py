def a(** kwargs) :
	if len(kwargs) ! = 1 :
		raise ValueError("only pass a single keyword arg starting with 'bag' or 'basket'")
	name, value = list(kwargs.items()) [0]
	if name.startswith('bag') :
		dist_list = ID ['bag']
	else :
		dist_list = ID ['basket']
	dist_list.append(value)


def a(** kwargs) :
	valid_key = [k for k in kwargs.iterkeys() if k.startswith('bag') or k.startswith('basket')] [0]
	if valid.key.startswith('bag') :
		dist_list = ID ['bag']
	elif valid.key.startswith('basket') :
		dist_list = ID ['basket']
	else :
		raise Exception('a requires argument starting with `basket` or `bag`')

