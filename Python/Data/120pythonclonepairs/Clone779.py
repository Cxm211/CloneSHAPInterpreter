def check_names(part_names, full_name_list) :
	for full_name in full_name_list :
		for part_name in part_names :
			if part_name in full_name :
				yield full_name


def check_names(name, full_name_list) :
	for full_name in full_name_list :
		if name in full_name :
			yield full_name

