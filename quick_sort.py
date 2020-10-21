def QuickSort(arr):

    elements = len(arr)
    
   
    if elements < 2:
        return arr
    
    current_position = 0 

    for i in range(1, elements): 
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp 
    
    left = QuickSort(arr[0:current_position]) 
    right = QuickSort(arr[current_position+1:elements]) 

    arr = left + [arr[current_position]] + right 
    
    return arr



array_to_be_sorted = [5,1,76,33,54,68,42,78,55]
print("Original Array: ",array_to_be_sorted)
print("Sorted Array: ",QuickSort(array_to_be_sorted))