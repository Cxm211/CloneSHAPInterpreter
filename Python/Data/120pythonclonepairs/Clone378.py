def call_api(url, data) :
	for k, value in list(data.items()) :
		url, n = re.subn(r'\{%s\}' % k, ';'.join(str(x) for x in value), url)
		if n :
			del data [k]


def call_api(url, data) :
	unused_keys = set()
	for k, value in data.items() :
		key_pattern = "{" + k + "}"
		if key_pattern in url :
			formatted_value = ';'.join(map(str, value))
			url = url.replace(key_pattern, formatted_value)
		else :
			unused_keys.add(k)

