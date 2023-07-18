def save(self, * args, ** kwargs) :
	if self.image_url :
		import urllib, os
		from urlparse import urlparse
		file_save_dir = self.upload_path
		filename = urlparse(self.image_url).path.split('/') [- 1]
		urllib.urlretrieve(self.image_url, os.path.join(file_save_dir, filename))
		self.image = os.path.join(file_save_dir, filename)
		self.image_url = ''
	super(tweet_photos, self).save()


def save(self, * args, ** kwargs) :
	if self.image_link and not self.image :
		result = urllib.urlretrieve(self.image_link)
		self.image.save(os.path.basename(self.image_link), File(open(result [0], 'r')))
		self.save()
		super(Pin, self).save()

