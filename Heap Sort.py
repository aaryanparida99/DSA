#Heapsort function creates a max-heap by calling max-heapify function and the sorts it
def heapsort(arr,n):
    for i in range(n//2,-1,-1):
        max_heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[0] , arr[i] = arr[i] , arr[0]
        max_heapify(arr,i,0)     


#max_heapify function is used to make the heap compliant to max heap rule
def max_heapify(arr,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    if right <n and arr[largest] < arr[right]:
        largest = right
    if(largest != i):
        arr[i] , arr[largest] = arr[largest] , arr[i]
        max_heapify(arr, n, largest)


#Driver Code
arr = [16,14,2,99,13,1,34,113,192,3,8]
n = len(arr)
heapsort(arr,n)
print(arr)