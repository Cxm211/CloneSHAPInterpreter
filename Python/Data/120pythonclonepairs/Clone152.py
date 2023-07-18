def type(text, delay) :
	i = 0
	amount = len(text)
	while amount < i :
		sys.stdout.write(text [i])
		sys.stdout.flush()
		i += 1
		time.sleep(delay)


def type(text, delay) :
	for beep in text :
		print(beep, end = "")
		sys.stdout.flush()
		time.sleep(delay)

