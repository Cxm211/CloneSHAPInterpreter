def run(self) :
	self.process = subprocess.Popen(self.cmd, stdout = self.outFile, stderr = self.errFile)
	while (self.process.poll() is None and self.timeout > 0) :
		time.sleep(1)
		self.timeout -= 1
	if not self.timeout > 0 :
		self.process.terminate()
		self.timed_out = True
	else :
		self.timed_out = False


def run(cmd, timeout_sec) :
	proc = subprocess.Popen(shlex.split(cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	timeout = {"value" : False}
	timer = Timer(timeout_sec, kill_proc, [proc, timeout])
	timer.start()
	stdout, stderr = proc.communicate()
	timer.cancel()
	return proc.returncode, stdout.decode("utf-8"), stderr.decode("utf-8"), timeout ["value"]

