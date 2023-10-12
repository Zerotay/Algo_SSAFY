import bisect

n = int(input())
lst = [*map(int, input().split())]
dp = [lst[0]]

for i in range(n):
    if lst[i] > dp[-1]:
        dp.append(lst[i])
    else:
        idx = bisect.bisect_left(dp, lst[i])
        dp[idx] = lst[i]

print(len(dp))
