def main() :
	n = int(raw_input())
	for i in range(0, 1 < < n) :
		gray = i ^ (i >> 1)
		print "{0:0{1}b}".format(gray, n),


def main() :
	n = int(raw_input())
	g = gray_code(n)
	if n > = 1 :
		for i in range(len(g)) :
			print g [i],

