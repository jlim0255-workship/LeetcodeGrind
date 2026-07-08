"""
coin change 2

we have a set of coins = {c1, c2, .. ck} and a target sum of money m

Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin and that each value in coins is unique.

coins = {1, 4, 5}
target sum = 13

define problem:
minimum_coins(coins, m) returns the minimum number of coins required for a sum m


base case:
minimum_coins(coins, 0) = 0
"""
def change(amount, coins):
    # memoization
    # cache = {}
    # def dfs(i, a):

    #     # base case(s)
    #     # we can sum to the amount
    #     if a == amount:
    #         return 1
        
    #     # if we cannot sum to the amount
    #     if a > amount:
    #         return 0
        
    #     # index out of bound, return 0
    #     if i == len(coins):
    #         return 0
        
    #     # its already exsists
    #     if (i, a) in cache:
    #         return cache[(i, a)]
        
    #     # go right and go down
    #     # dfs(i, a + coins[i]) -> go right, a is current amount + coins[i], go coins[i] steps to the right

    #     # dfs(i + 1, a) -> go to the next coin (1 row below) at the same amount level
    #     cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)

    #     return cache[(i, a)]
    
    # return dfs(0,0)

    # dp way (2D array)
    dp= [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)

    for a in range(1, amount + 1):
        for i in range(len(coins)-1, -1, -1):
            dp[a][i] = dp[a][i+ 1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]
    return dp[amount][0]