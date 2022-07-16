def selec_sort(arr):
    for i in range(0,len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]


#Driver Code
arr = [16,14,2,99,13,1,34,113,192,3,8]
n = len(arr)
selec_sort(arr)
print(arr)