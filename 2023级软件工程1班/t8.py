# w = [1,1,1,4] v = [3,9,6,2] n = 4 W = 6
def kanp(w, v, capacity):  # w:物品重量,v:物品价值,n:物品个数,capacity:背包容量
    global dp  # dp表
    n = len(w)
    # [0] * (capacity + 1)这是确保每一列均为[0]构成,for i in range(n + 1)循环n+1行,所以每n+1行都有capacity+1列个[0]
    dp = [[8] * (capacity + 1) for i in range(n + 1)]# 创造dp表
    for row in range(0,n+1):
        dp[row][0] = 0
    for col in range(0,capacity+1):
        dp[0][col] = 0
    print(dp)
    # 使用状态转移方程将8贴换为价值的累计和
    for row in range(1, n + 1): # 遍历行
        for col in range(1, capacity + 1): # 遍历列
            # 装不下
            if col < w[row - 1]:# rw是剩余容量,w[row - 1]是当前物品的重量
                dp[row][col] = dp[row - 1][col]
            # 装得下
            else:
                # v[row - 1]是当前物品的价值,
                # dp[row - 1][col - w[row - 1]]是不选择当前物品之前的累计价值,
                # dp[row - 1][col - w[row - 1]] + v[row - 1]是选择当前物品后的累计价值.
                dp[row][col] = max(dp[row - 1][col], dp[row - 1][col - w[row - 1]] + v[row - 1])
    return dp[n][capacity]        
w = [1,1,1,4] 
v = [3,9,6,2] 
capacity = 6
result = kanp(w, v, capacity)
print(result)
"""
[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

[
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0]
]

[[0, 8, 8, 8, 8, 8, 8],
 [0, 8, 8, 8, 8, 8, 8], 
 [0, 8, 8, 8, 8, 8, 8], 
 [0, 8, 8, 8, 8, 8, 8], 
 [8, 8, 8, 8, 8, 8, 8]]

 [
 [0, 0, 0, 0, 0, 0, 0], 
 [0, 8, 8, 8, 8, 8, 8], 
 [0, 8, 8, 8, 8, 8, 8], 
 [0, 8, 8, 8, 8, 8, 8], 
 [0, 8, 8, 8, 8, 8, 8]]
"""
