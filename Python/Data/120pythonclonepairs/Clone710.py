def wrapper(* args, ** kwargs) :
	for i in range(max_retries + 1) :
		print ('Try #', i + 1)
		try :
			return fn(* args, ** kwargs)
		except exception_type as e :
			print ('wrapper exception:', i + 1, e)


def wrapper(* args, ** kwargs) :
	assert max_retries > 0
	x = max_retries
	while x :
		try :
			return func(* args, ** kwargs)
		except ex :
			x -= 1

