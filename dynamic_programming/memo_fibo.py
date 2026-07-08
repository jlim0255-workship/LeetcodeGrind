# normal fibo
def fibo(n):
    if n <= 2:
        # base case fibo(0) and fibo(1) = 1
        result = 1
    else:
        result = fibo(n-1) + fibo(n-2)
    return result

# recursion with memo
memo = {}
def memo_fibo(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        # base case fibo(0) and fibo(1) = 1
        result = 1
    else:
        result = memo_fibo(n-1) + memo_fibo(n-2)

    memo[n] = result

    return result

# bottom up approach with for loop
def fib_bottom_up(n):
    memo = {}

    for i in range(1, n + 1):
        if i <= 2:
            result = 1
        else:
            result = memo[i-1]+ memo[i-2]

        memo[i] = result

    return memo[n]

if __name__ == "__main__":
    print(fibo(20))
    print(memo_fibo(20))
