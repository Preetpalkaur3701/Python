from collections import Counter

def binaryAnagram(n1,n2):
    #converting n1 and n2 into binary
    bin1 = bin(n1)[2:]
    bin2 = bin(n2)[2:]

    # append zeros in shorter string 
    zeros = abs(len(bin1)-len(bin2)) 
    if (len(bin1)>len(bin2)): 
         bin2 = zeros * '0' + bin2 
    else: 
         bin1 = zeros * '0' + bin1 
    
    #convert binary representations into dictionary 
    dict1 = Counter(bin1) 
    dict2 = Counter(bin2) 
    if dict1 == dict2: 
         print('Yes') 
    else: 
         print('No') 
n1 = int(input("First Number: "))
n2 = int(input("Second Number: "))

binaryAnagram(n1,n2)