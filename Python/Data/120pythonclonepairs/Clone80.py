def pdf_view(request) :
	with open('/path/to/my/file.pdf', 'r') as pdf :
		response = HttpResponse(pdf.read(), mimetype = 'application/pdf')
		response ['Content-Disposition'] = 'inline;filename=some_file.pdf'
		return response
	pdf.closed


def pdf_view(request) :
	try :
		return FileResponse(open('foobar.pdf', 'rb'), content_type = 'application/pdf')
	except FileNotFoundError :
		raise Http404()

