def knapsack2(w_items, c_items, w, n):
    dp = [[0 for i in range(w + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(w + 1):
            dp[i][j] = dp[i - 1][j]

            if j >= w_items[i - 1] and dp[i][j] < dp[i - 1][j - w_items[i - 1]] + c_items[i - 1]:
                dp[i][j] = dp[i - 1][j - w_items[i - 1]] + c_items[i - 1]

    w_cnt = w
    items = []
    for i in range(n, 0, -1):
        if dp[i][w_cnt] != dp[i - 1][w_cnt]:
            items.append(i - 1)
            w_cnt -= w_items[i - 1]

    return dp[n][w], w - w_cnt, set(items)


profit = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
weight = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
W = 165
n = len(profit)

best_profit, total_weight, items = knapsack2(weight, profit, W, n)

print('best profit:', best_profit)
print('picked items:', items)
print('total weight:', total_weight)