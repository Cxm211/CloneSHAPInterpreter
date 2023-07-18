def deep_get(d, keys, default = None) :
	assert type(keys) is list
	if d is None :
		return default
	if not keys :
		return d
	return deep_get(d.get(keys [0]), keys [1 :], default)


def deep_get(_dict, keys, default = None) :
	def _reducer(d, key) :
		if isinstance(d, dict) :
			return d.get(key, default)
		return default
	return reduce(_reducer, keys, _dict)

