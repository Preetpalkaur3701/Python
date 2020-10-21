# Python program for Bitonic Sort. Note that this program
# works only when size of input is a power of 2.

# The parameter direction indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.
def compAndSwap(array, i, j, direction):
    if (
        direction == 1 and array[i] > array[j]
    ) or (
        direction == 0 and array[i] < array[j]
    ):
        array[i], array[j] = array[j], array[i]


# if direction = 1, and in descending order otherwise (means direction=0).
# The sequence to be sorted starts at index position low,
# the parameter array_length is the number of elements to be sorted.
def bitonic_merge(array, low_index, array_length, direction):
    if array_length > 1:
        k = int(array_length / 2)
        for i in range(low_index, low_index + k):
            compAndSwap(array, i, i + k, direction)
        bitonic_merge(array, low_index, k, direction)
        bitonic_merge(array, low_index + k, k, direction)


# sorting its two halves in opposite sorting orders, and then
# calls bitonic_merge to make them in the same order
def bitonic_sort(a, low_index, array_length, direction):
    if array_length > 1:
        k = int(array_length / 2)
        bitonic_sort(a, low_index, k, 1)
        bitonic_sort(a, low_index + k, k, 0)
        bitonic_merge(a, low_index, array_length, direction)


if __name__ == "__main__":

    array = [2, 3, 4, 6, 10, 1, 8, 7, 9, 5]
    low_index = 0
    array_length = 10
    direction = 1

    bitonic_sort(array, low_index, array_length, direction)
    print(array)
