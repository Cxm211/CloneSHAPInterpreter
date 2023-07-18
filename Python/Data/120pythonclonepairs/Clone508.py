def prime(n) :
	for x in range(2, int(math.sqrt(n)) + 1) :
		if n % x == 0 :
			print n / x
			return prime(n / x)


def prime(n, a) :
	i = a
	while (n % i ! = 0 and i * i < n) :
		i += 1
	if (i * i < n) :
		return prime(n / i, i)
	else :
		print ("The highest prime factor is: "), n

