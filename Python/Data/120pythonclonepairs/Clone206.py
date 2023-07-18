def greet(lines, cheers) :
	for i in range(lines) :
		output = (" ") * i + "Go"
		for j in range(cheers) :
			if cheers == 1 :
				print output
				break
			output += "Budddy Go"
		print output


def greet(lines, cheers) :
	i = 0
	line_str = ""
	while i < cheers :
		i += 1
		line_str += "GO" if i == cheers else "GO BUDDY "
	i = 0
	while i < lines :
		print (" " * (i * 3) + line_str)
		i += 1

