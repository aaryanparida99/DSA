def countSort(arr,n,place):
    #assuming max element are in range 0-10
    count_arr = [0] * 10
    res = [0] * n
    for i in range(n):
        index = arr[i] // place
        count_arr[index%10] += 1
    
    for i in range(1,10):
        count_arr[i] += count_arr[i-1]
    
    for i in range(n-1,-1,-1):
        index = arr[i] // place
        res[count_arr[ index % 10 ] - 1 ] = arr[i]
        count_arr[index % 10] -= 1

    for i in range(n):
        arr[i] = res[i]

def radixSort(arr,n):
    max_ele = max(arr)
    place = 1
    while max_ele // place > 0:
        countSort(arr, n, place)
        place *= 10


arr = [131, 12, 9, 171, 11, 2, 4]
n = len(arr)
radixSort(arr,n)
print(arr)