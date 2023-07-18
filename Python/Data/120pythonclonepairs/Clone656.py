def default(self, obj) :
	try :
		return super(DatetimeEncoder, obj).default(obj)
	except TypeError :
		return str(obj)


def default(self, obj) :
	if isinstance(obj, datetime.datetime) :
		encoded_object = list(obj.timetuple()) [0 : 6]
	else :
		encoded_object = json.JSONEncoder.default(self, obj)
	return encoded_object

