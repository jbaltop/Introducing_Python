def is_none(thing):
	if thing is None:
		print("It's None")
	elif thing:
		print("It's True")
	else:
		print("It's False")
is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
is_none([])
is_none({})
is_none(set())
