def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)]
    selected = [0 for i in range(W+1)]
    
    for i in range(1, n+1):
        for w in range(W, 0, -1):
            if wt[i-1] <= w:
                if dp[w] < dp[w-wt[i-1]] + val[i-1]:
                    dp[w] = dp[w-wt[i-1]] + val[i-1]
                    selected[w] = i - 1
    
    result = []
    i = W
    while i != 0:
        result.append(selected[i])
        i -= wt[selected[i]]
    
    return dp[W], result

profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(profit)

max_profit, selected_items = knapSack(W, weight, profit, n)
print("Dhruv Varshney \nA2305221157")
print("Maximum profit that can be obtained:", max_profit)
print("Selected items:", selected_items)