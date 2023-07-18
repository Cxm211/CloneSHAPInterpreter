def fib(a = 0, b = 1) :
	yield a
	while True :
		yield b
		a, b = b, a + b


def fib(n) :
	a, b = 0, 1
	for i in range(n) :
		a, b = b, a + b
	return a

