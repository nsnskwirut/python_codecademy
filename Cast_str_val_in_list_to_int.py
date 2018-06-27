#!/opt/ute/python/bin/python


def value_caster(string):
	try:
		if "." not in string:
			n = int(string)
		else:
			n = float(string)
	except ValueError:
		n = -9999
	finally:
		return n

dupa = "-1"

print value_caster(dupa)