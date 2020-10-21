def countsort(arr):
    output = [0 for i in range(len(arr))]

    count = [0 for i in range(256)]
    ans = ["" for _ in arr]

    for i in arr:
        count[ord(str(i))] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[ord(str(arr[i]))] - 1] = arr[i]
        count[ord(str(arr[i]))] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


arr = []

arr_length = input("How many numbers will be there in the array:")

print("Enter the numbers in the array...")
for n in range(int(arr_length)):
    num = input("num" + str(n + 1) + ":")
    arr.append(int(num))

print("Your array is:", arr)

ans = countsort(arr)
print("Sorted character array is % s" % ("".join(str(ans))))
