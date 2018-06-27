#!/opt/ute/python/bin/python


eq = {'rope': 1,
      'torch': 6,
      'gold coin': 42,
      'dagger': 1,
      'arrow': 12}
dragon_loot =  ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(my_inv_dic):
	v_total = 0
	for k, v in my_inv_dic.items():
		v_total += v
		print("{0}: {1}".format(k,v))
	print("----------\ntotal: {}".format(v_total))

def add_to_inventory(my_inv_dic, enemy_inv_list):
	for item in enemy_inv_list:
		print("---adding: {}".format(item)) # Do testu
		if item not in my_inv_dic:
			my_inv_dic.update({item: 1})
		else:
			my_inv_dic[item] += 1
	return my_inv_dic

#Test
print "\neq na poczatku"
display_inventory(eq)
print "\ndodaje loot:"
print add_to_inventory(eq, dragon_loot)
print "\neq po dodaniu lootu:"
display_inventory(eq)

