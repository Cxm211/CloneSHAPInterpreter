def emit(self, record) :
	if record.exc_info :
		record.exc_text = self.formatException(record.exc_info)
		record.exc_info = None
	self.queue.put(record)


def emit(self, record) :
	try :
		s = self._format_record(record)
		self.send(s)
	except (KeyboardInterrupt, SystemExit) :
		raise
	except :
		self.handleError(record)

