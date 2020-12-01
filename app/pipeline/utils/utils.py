def printing_progress(func):
	def wrapper_printing_progress(*args, **kwargs):
		print("in progress ...")
		func(*args, **kwargs)
	return wrapper_printing_progress

