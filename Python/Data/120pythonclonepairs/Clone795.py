def encrypt(key, plaintext) :
	padded_key = key.ljust(KEY_SIZE, '\0')
	padded_text = plaintext + (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * '\0'
	r = rijndael.rijndael(padded_key, BLOCK_SIZE)
	ciphertext = ''
	for start in range(0, len(padded_text), BLOCK_SIZE) :
		ciphertext += r.encrypt(padded_text [start : start + BLOCK_SIZE])
	encoded = base64.b64encode(ciphertext)
	return encoded


def encrypt(key, plaintext) :
	key = key.encode('ascii')
	plaintext = plaintext.encode('utf-8')
	padded_key = key.ljust(KEY_SIZE, b'\0')
	sg = pprp.data_source_gen(plaintext, block_size = BLOCK_SIZE)
	eg = pprp.rjindael_encrypt_gen(padded_key, sg, block_size = BLOCK_SIZE)
	ciphertext = pprp.encrypt_sink(eg)
	encoded = base64.b64encode(ciphertext)
	return encoded.decode('ascii')

