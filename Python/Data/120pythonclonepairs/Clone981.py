def myfunc(orientation, l, w) :
	if 1 < = orientation < = 8 :
		a = (- w, - l, - w, - l, w, l, w, l) [orientation - 1]
		b = (l, w, - l, - w) [(orientation - 1) % 4]
	return a, b


def myfunc(orientation, l, w) :
	a, b = (w, l) if orientation % 2 else (l, w)
	if orientation < = 4 :
		a = - a
	if orientation in (3, 4, 7, 8) :
		b = - b
	return a, b

