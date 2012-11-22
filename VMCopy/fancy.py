def cyclic():
	if not hasattr(cyclic, "character"):
		cyclic.character = '|'
	if cyclic.character == '|':
		cyclic.character =  '/'
	elif cyclic.character == '/':
		cyclic.character = '-'
	elif cyclic.character == '-':
		cyclic.character =  '\\'
	else:
		cyclic.character = '|'
	return cyclic.character
