def n_letter_dictionary(string) :
	result = {}
	for key, group in groupby(sorted(string.split(), key = lambda x : len(x)), lambda x : len(x)) :
		result [key] = list(group)
	return result


def n_letter_dictionary(my_string) :
	my_string = my_string.lower().split()
	sample_dictionary = {}
	for word in my_string :
		if len(word) not in sample_dictionary :
			sample_dictionary [len(word)] = set()
		sample_dictionary [len(word)].add(word)
	return sample_dictionary

