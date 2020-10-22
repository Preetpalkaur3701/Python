import string

dict={}
data = ""

# create a file to store the output

file = open("output.txt", "w")
for i in range(len(string.ascii_letters)):

#exchanging the letters

	dict[string.ascii_letters[i]] = string.ascii_letters[i-1]
print (dict)
with open ("text.txt") as f:
	while True:
		c = f.read(1)
		if not c:
			print ("End of this file")
			break
		if c in dict:
			data = dict[c]
		else:
			data = c
		file.write(data)
		print (data)
file.close()