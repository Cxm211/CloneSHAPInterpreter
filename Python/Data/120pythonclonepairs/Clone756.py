def checkLen() :
	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	if "Monday" in days :
		print "found"
		print days.index("Monday")


def checkLen() :
	days = ["Monday", "Tuesday", "Wednesday", "Thursday" "Friday", "Saturday", "Sunday"]
	try :
		position = days.index("Monday")
		print ("Found it")
	except ValueError :
		position = None
		print ("Not present")
	print (position)

