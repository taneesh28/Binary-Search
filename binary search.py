from array import *

n = int(input("enter the size on an array"))
arr = ([])
for i in range(n):
    x = int(input("Enter the Next Value"))
    arr.append(x)
print(arr)

val = int(input("enter the element you want to search"))


def b_search(arr, val):
    i = arr[0]
    j = arr[-1]
    mid = int(i + j) / 2
    while (i <= j):
        for z in range(n):
            if (val == arr[z]):
                print("Search complete, YOur value found at", arr[z])
                mid = 0
            elif (val < arr[z]):
                print("still Searching your value on right side ", arr[z])
                j = mid - 1
            else:
                print("still Searching your value on left side", arr[z])
                i = mid + 1


b_search(arr, val)
