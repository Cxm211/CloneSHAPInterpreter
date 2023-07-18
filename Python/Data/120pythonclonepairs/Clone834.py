def find_solution(low, high) :
	for num in xrange(low, high + 1) :
		lst = find_prime_factors(num)
		for n, count in lst :
			pf [n] = max(pf [n], count)
	print "prime factors:", pf
	solution = 1
	for n, count in pf.items() :
		solution *= n ** count
	return solution


def find_solution(step) :
	for num in xrange(step, 999999999, step) :
		if all(num % n == 0 for n in check_list) :
			return num
	return None

