def after_request(response) :
	diff = time.time() - g.start
	if app.debug :
		print "Exec time: %s" % str(diff)
	if (response.response) :
		response.response [0] = response.response [0].replace('__EXECUTION_TIME__', str(diff))
		response.headers ["content-length"] = len(response.response [0])
	return response


def after_request(response) :
	diff = time.time() - g.start
	if ((response.response) and
	(200 < = response.status_code < 300) and
	(response.content_type.startswith('text/html'))) :
		response.set_data(response.get_data().replace(
		b'__EXECUTION_TIME__', bytes(str(diff), 'utf-8')))
	return response

