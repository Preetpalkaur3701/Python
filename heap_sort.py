#  Python program for implementation of Heap Sort 
def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[i] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]

		heapify(arr, n, largest)


def heap_sort(arr):
	n = len(arr)

	for i in range(n, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)


arr = [13, 10, 12, 5, 6, 7, 2, 16, 11]
print("Array Before Sort: ",arr)
heap_sort(arr)
print("Sorted array: ", arr)

'''
Ouput:
Array Before Sort:  [13, 10, 12, 5, 6, 7, 2, 16, 11]
Sorted array:  [2, 5, 6, 7, 10, 11, 12, 13, 16] '''
