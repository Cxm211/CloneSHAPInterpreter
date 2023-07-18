def count_char(text) :
	answer = {}
	for char in text :
		if char in answer :
			answer [char] += 1
		else :
			answer [char] = 1
	print (answer)


def count_char(text) :
	for char in string.ascii_letters :
		count = text.count(char)
		if count :
			print (char + ' = ' + str(count))

