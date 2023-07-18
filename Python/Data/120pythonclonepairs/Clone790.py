def __exit__(self, et, ev, tb) :
	if self.level is not None :
		self.logger.setLevel(self.old_level)
	if self.handler :
		self.logger.removeHandler(self.handler)
	if self.handler and self.close :
		self.handler.close()


def __exit__(self, exception_type, exception_value, traceback) :
	self.restore_logger('', logging.getLogger())
	for name, logger in logging.Logger.manager.loggerDict.items() :
		self.restore_logger(name, logger)

