def decorator(function) :
	if after :
		return afterDecorator(function, event)
	else :
		return beforeDecorator(function, event)


def decorator(f) :
	@ wraps(f)
	def wrapped(* args, ** kargs) :
		result = f(* args, ** kargs)
		event.fire(* args, ** kargs)
		return result
	return wrapped

