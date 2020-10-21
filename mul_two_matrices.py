# input two matrices of size n x m 
matrix1 = [[3,7,3], 
        [6 ,5,6], 
        [70 ,10,9]] 
matrix2 = [[50,0,1], 
        [66,7,33], 
        [64,55,92]] 
  
res = [[0 for x in range(3)] for y in range(3)]  
  
# explicit for loops 
for i in range(len(matrix1)): 
    for j in range(len(matrix2[0])): 
        for k in range(len(matrix2)): 
  
            # resulted matrix 
            res[i][j] += matrix1[i][k] * matrix2[k][j] 
  
print (res) 