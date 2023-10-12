# 14719 빗물 (G5)
# https://www.acmicpc.net/problem/14719
# 정답

h,w = map(int,input().split())
inlst = [*map(int,input().split())]
ans = 0
for i in range(1, w-1):
    tmp = min(max(inlst[:i]),max(inlst[i+1:])) - inlst[i]
    ans += tmp if tmp>0 else 0
print(ans)

# 원리만 연상하면 쉽지만, 그게 쉽지 않았던 문제
# 각 위치마다 고일 물의 양을 생각해보기
# 자신의 위치와 자신보다 높은 옆의 높이를 고려하면 됨
# 열의 개수에 따라 시간복잡도가 고정됨
# 498 * 499 대략 250000