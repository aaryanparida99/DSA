def jobScheduling(arr,max_job):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j][2] < arr[j+1][2]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

    job = ['-1'] * max_job
    res = [False] * max_job

    for i in range(n):
        for j in range(min(max_job -1 , arr[i][1] - 1), -1 , -1):
            if res[j] is False:
                res[j] = True
                job[j] = arr[i][0]
                break
    print(job)



#Driver Code
arr = [
    ['J1', 5 , 50],
    ['J2', 3, 60],
    ['J3', 2, 70],
    ['J4', 4 , 55],
    ['J5', 3 , 65],
    ['J6', 2 , 75],
    ['J7', 3, 90]
    ]

jobScheduling(arr,5)