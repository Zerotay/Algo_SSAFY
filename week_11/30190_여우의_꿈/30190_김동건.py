# 30190 여우의 꿈 (G5)
# https://www.acmicpc.net/problem/30190
# 정답

# n,k = map(int, input().split())
# lst = [*map(int,input().split())]
# mod = 10**9+7
# dp = [0]*(n+1)
# for i in range(1, n+1): dp[i] = ((dp[i-1] * 2) % mod + 1) % mod
# ans = 0
# for i,j in reversed(list(enumerate(lst))):
#     if k != j:
#         k = 6-k-j
#         ans += 1 + (dp[i] if i else 0)
# print(ans % mod)

n,k = map(int, input().split())
lst = [*map(int,input().split())]
mod = 10**9+7
dp = [1]*n
for i in range(1,n): dp[i] = (dp[i-1]*2) % mod
ans = 0
for i in range(n-1,-1,-1):
    if k != lst[i]:
        k = 6-k-lst[i]
        ans += dp[i]
print(ans % mod)

# dp로 하노이 공식 사용하기
# 특정 층의 원판은 이미 자기 자리인 경우가 아니라면 자기 위의 모든 원판을
# 일단 다른 곳으로 보낸 후에 자신이 이동해야 한다.
# 그래서 자신 위의 원판을 완벽하게 다른 곳으로 보내는 횟수에 1을 더해주면 된다.

# dp배열은 자기 위치에서 이동을 해야할 경우, 자신의 위 원판들을 다른 곳으로 옮겨두는 횟수
# 원판을 아래에서부터 원하는 위치로 옮겨야 하며, 이후에 원판이 어디에 옮겨졌는지 업데이트해야만 한다.
