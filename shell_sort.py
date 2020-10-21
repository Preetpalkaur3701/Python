def shellsort(arr):
    length = len(arr)
    gap = int(length / 2)

    while gap > 0:

        for i in range(gap, length):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

                # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap = int(gap / 2)
    return arr


arr = []

arr_length = input("How many numbers will be there in the array:")

print("Enter the numbers in the array...")
for n in range(int(arr_length)):
    num = input("num" + str(n + 1) + ":")
    arr.append(int(num))

print("Your array is:", arr)

print("Sorted character array is:", shellsort(arr))
