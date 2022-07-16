def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    
    
#Driver Code
arr = [16,14,2,99,13,1,34,113,192,3,8]
n = len(arr)
bubblesort(arr)
print(arr)