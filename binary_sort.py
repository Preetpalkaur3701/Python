def binary_insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        pos = binary_search(alist, temp, 0, i) + 1
 
        for k in range(i, pos, -1):
            alist[k] = alist[k - 1]
 
        alist[pos] = temp
 
def binary_search(alist, key, start, end):
 
    if end - start <= 1:
        if key < alist[start]:
            return start - 1
        else:
            return start
 
    mid = (start + end)//2
    if alist[mid] < key:
        return binary_search(alist, key, mid, end)
    elif alist[mid] > key:
        return binary_search(alist, key, start, mid)
    else:
        return mid
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
binary_insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)