# Append Dictionary Keys and Values ( In order ) in dictionary 
from itertools import chain 
# initializing dictionary 
my_dict = {"I" : 1, "am" :  3, "the" : 2, "BEST" : 4}
print("The original dictionary is : " + str(my_dict)) 
#appending the dictionary 
new_dict = list(chain(my_dict.keys(), my_dict.values()))
print("The ordered keys and values : " + str(new_dict))  




