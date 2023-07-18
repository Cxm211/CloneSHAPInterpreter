def fib(n) :
	if n < = 2 :
		return 1
	else :
		return fib(n - 1) + fib(n - 2)


def fib(n) :
	a, b = decimal.Decimal(0), decimal.Decimal(1)
	for i in decimal_range(0, n) :
		a, b = b, a + b
	return a

