# function definition
def dictionairy(): 

	# Declaring the hash function	 
	key_value ={}	 

	# Initialize values
	key_value[2] = "How"
	key_value[1] = "Hello"
	key_value[5] = "?"
	key_value[4] = "You"
	key_value[6] = "!"	
	key_value[3] = "Are"

	print ("Keys and Values sorted in alphabetical order by key \n") 

	# sorted(key_value) returns an iterator over the 
	# Dictionary’s value sorted in keys. 
	for i in sorted (key_value) : 
		print ((i, key_value[i]), end =" ") 

def main(): 
	# function calling 
	dictionairy()			 
	
# main function calling 
if __name__=="__main__":	 
	main() 



