#!/opt/ute/python/bin/python

tableData = [['appeeeeeeeeles', 'oranges', 'cherries', 'banaeeena', 'fruit'],
             ['Alice', 'Bob', 'Careeeol', 'David', 'name'],
             ['dogs', 'caeeets', 'moose', 'gose', 'animeeal']]


# Zamienia [[a,1,X],[b,2,Y],[c,3,Z]] na [[a,b,c],[1,2,3],[X,Y,Z]]
def transpose(input_list):
    return map(list, zip(* input_list))


def determine_longest(input_list):
	col_widths = []
	for i in range(len(input_list)):
		max_len = 0
		for item in input_list[i]:
			if len(item) > max_len:
				max_len = len(item)
		col_widths.append(max_len)
	return col_widths


def print_table(input_list):
	col_widths = determine_longest(transpose(input_list))
	print("Col widths: {}".format(col_widths))
	for list_ in input_list:
		for i in range(len(col_widths)):
			list_[i] = (col_widths[i] - len(list_[i])) * " " + list_[i]
		print " | ".join(list_)


# print transpose(tableData)
print_table(transpose(tableData))
