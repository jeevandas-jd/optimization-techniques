def tsp_dynamic_programming(dist):
    import math


    n = len(dist)

    dp = [[math.inf] * n for _ in range(1 << n)]

    dp[1][0] = 0

    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue

            for j in range(n):
                if j == i or not (mask & (1 << j)):
                    continue
                dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][j] + dist[j][i])
    full_mask = (1 << n) - 1
    min_cost = min(dp[full_mask][i] + dist[i][0] for i in range(1, n))

    return min_cost
