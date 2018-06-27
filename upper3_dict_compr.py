#!/opt/ute/python/bin/python

def upper3_to_dict(list_):
	new_dict = {c[:3].upper(): c for c in list_}
	return new_dict



