def date_hook(json_dict) :
	for (key, value) in json_dict.items() :
		try :
			json_dict [key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
		except :
			pass
	return json_dict


def date_hook(json_dict) :
	for (key, value) in json_dict.items() :
		if type(value) is str and re.match('^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d*$', value) :
			json_dict [key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
		elif type(value) is str and re.match('^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$', value) :
			json_dict [key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
		else :
			pass
	return json_dict

