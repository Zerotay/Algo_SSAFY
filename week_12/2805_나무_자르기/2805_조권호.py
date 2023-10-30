# 2805 나무 자르기 (S2)
# https://www.acmicpc.net/problem/2805
# 정답

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 1, max(trees)
while left <= right:
    ans = 0
    mid = (left + right) // 2
    for i in trees:
        if i >= mid:
            ans += i - mid
    if ans >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)
