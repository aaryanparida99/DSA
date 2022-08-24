def quickSort(arr,p,q):
    if (p==q):
        return arr
    elif(q>p):
        m = partition(arr,p,q)
        quickSort(arr, p, m-1)
        quickSort(arr, m+1, q)
    return arr


def partition(a,p,q):
    key = arr[p]
    i = p
    for j in range(p+1,q):
        if arr[j] < key:
            i=i+1
            arr[j] , arr[i] = arr[i] ,arr[j]
    arr[p] , arr[i] = arr[i] , arr[p]
    return i

#Drivercode
arr = [5,6,2,12,80,1]
p=0
q=6
quickSort(arr, p, q)
print(arr)
            

