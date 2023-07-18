def censored(sentence, bad_words = EXCLUDED_WORDS) :
	if bad_words :
		for word in bad_words :
			sentence = sentence.replace(word, '*' * len(word))
	return sentence


def censored(sentence, words) :
	for word in words :
		if word in sentence :
			sentence = sentence.replace(word, "*" * len(word))
	return sentence

