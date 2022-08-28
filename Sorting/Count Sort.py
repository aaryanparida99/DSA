def countSort(arr,n):
    #assuming max element are in range 0-10
    count_arr = [0] * 10
    res = [0] * n
    for i in range(n):
        count_arr[arr[i]] += 1
    
    for i in range(1,10):
        count_arr[i] += count_arr[i-1]
    
    for i in range(n-1,-1,-1):
        res[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -= 1
    print(res)




arr = [5,6,7,2,9,3,1,2,8,8]
n = len(arr)
countSort(arr,n)
