def formatTime(self, record, datefmt = None) :
	arrow_time = Arrow.fromtimestamp(record.created)
	if datefmt :
		arrow_time = arrow_time.format(datefmt)
	return str(arrow_time)


def formatTime(self, record, datefmt = None) :
	ct = self.converter(record.created)
	if datefmt :
		s = ct.strftime(datefmt)
	else :
		t = ct.strftime("%Y-%m-%d %H:%M:%S")
		s = "%s,%03d" % (t, record.msecs)
	return s

