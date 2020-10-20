num_arr = []

arr_length = raw_input("How many numbers will be there in the array:")

print("Enter the numbers in the array...")
for i in range(int(arr_length)):
  # just added i values to num for num1, num2 etc
  num = raw_input("num"+str(i+1)+":")
  # append input values to our list
  num_arr.append(int(num))

print("Your array is:", num_arr)

for i in range(int(arr_length)):
  for j in range(int(arr_length)-i-1):
    if num_arr[j] > num_arr[j+1]:
      # swap the values
      num_arr[j], num_arr[j+1] = num_arr[j+1], num_arr[j]

print("Sorted Array: ", num_arr)