def quickSort(arr,low,high):
        if (low == high) :
            return arr
        elif(high>low):
            m = partition(arr,low,high)
            quickSort(arr,low,m-1)
            quickSort(arr,m+1,high)
        return arr
    
def partition(arr,low,high):
        key = arr[low]
        i = low
        for j in range(low+1,high):
            if key > arr[j]:
                i = i+1
                arr[j] , arr[i] = arr[i] , arr[j]
        arr[i] , arr[low] = arr[low] , arr[i]
        return i

arr = [5,6,2,12,80,1]
p=0
q=6
quickSort(arr, p, q)
print(arr)