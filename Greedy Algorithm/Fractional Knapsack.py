def max_profit(weight,profit,n,m):
    res = 0
    pw_ratio = [( profit[i]/weight[i]) for i in range(n) ]
    weight_sorted = [ x for _ , x in sorted(zip(pw_ratio,weight), reverse=True)]
    profit_sorted = [ x for _ , x in sorted(zip(pw_ratio,profit), reverse=True)]
    for i in range(n):
        if m == 0:
            return res
        if weight_sorted[i] < m:
            res = res + profit_sorted[i]
            m = m - weight_sorted[i]
        else:
            
            ratio = m/weight_sorted[i]
            res = res + ratio*profit_sorted[i]
            m = 0
    return res





#Driver Code
n = 7
m = 37
weight = [5,10,12,4,7,9,3]
profit = [25,75,100,50,45,90,30]
max = max_profit(weight, profit,n,m)
print(max)