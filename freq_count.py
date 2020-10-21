def get_freq_count(items):
	freq_dict = {}
	for item in items:
		if item in freq_dict:
			freq_dict[item] += 1
		else:
			freq_dict[item] = 1
	return freq_dict

items = input('Enter the space separated items of the list: ').split()
freq_dict = get_freq_count(items)
for item in freq_dict:
	print("{} is appearing {} times in the list.".format(item, freq_dict[item]))
