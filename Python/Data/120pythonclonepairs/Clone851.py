def not_raises(exception) :
	try :
		yield
	except exception :
		raise pytest.fail("DID RAISE {0}".format(exception))


def not_raises(ExpectedException) :
	try :
		yield
	except ExpectedException, err :
		raise AssertionError(
		"Did raise exception {0} when it should not!".format(
		repr(ExpectedException)))
	except Exception, err :
		raise AssertionError(
		"An unexpected exception {0} raised.".format(repr(err)))

