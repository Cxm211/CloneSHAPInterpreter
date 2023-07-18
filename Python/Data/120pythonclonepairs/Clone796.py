def decrypt(key, encoded) :
	padded_key = key.ljust(KEY_SIZE, '\0')
	ciphertext = base64.b64decode(encoded)
	r = rijndael.rijndael(padded_key, BLOCK_SIZE)
	padded_text = ''
	for start in range(0, len(ciphertext), BLOCK_SIZE) :
		padded_text += r.decrypt(ciphertext [start : start + BLOCK_SIZE])
	plaintext = padded_text.split('\x00', 1) [0]
	return plaintext


def decrypt(key, encoded) :
	key = key.encode('ascii')
	padded_key = key.ljust(KEY_SIZE, b'\0')
	ciphertext = base64.b64decode(encoded.encode('ascii'))
	sg = pprp.data_source_gen(ciphertext, block_size = BLOCK_SIZE)
	dg = pprp.rjindael_decrypt_gen(padded_key, sg, block_size = BLOCK_SIZE)
	return pprp.decrypt_sink(dg).decode('utf-8')

