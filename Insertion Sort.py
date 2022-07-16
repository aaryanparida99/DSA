def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key


#Driver Code
arr = [16,14,2,99,13,1,34,113,192,3,8]
n = len(arr)
insertionSort(arr)
print(arr)