def min_steps(x, y):
    if x == y:
        return 0
    elif x + 1 == y:
        return 1
    else:
        dp = [0] * (y - x + 1)
        dp[1] = 1
        for i in range(2, y - x + 1):
            dp[i] = dp[i - 1] + 1
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i // 2] + 1)
            if (i - 1) % 2 == 0:
                dp[i] = min(dp[i], dp[(i - 1) // 2] + 2)
        return dp[-1]

# Приклади
x = int(input("Введіть число х: "))
y = int(input("Введіть число y: "))

print(f"Результат: {min_steps(x, y)}")
