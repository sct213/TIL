def solution(n):
    dp = [0, 1]

    for i in range(2, n + 1):
        dp.append((dp[i-1] + dp[i-2]) % 1234567)
        print(i, dp)

    return dp[n]


print(solution(3))