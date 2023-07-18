def __str__(self) :
	if self.cards :
		rep = ""
		for card in self.cards :
			rep += str(card) + "\t"
	else :
		rep = "<empty>"
	return rep


def __str__(self) :
	rep = self.name + "\t" + super(BJ_hand, self).__str__()
	if self.total :
		rep += "(" + str(self.total) + ")"
	return rep

