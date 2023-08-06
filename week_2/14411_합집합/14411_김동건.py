# 14411 합집합 (G4)
# https://www.acmicpc.net/problem/14411
# 정답

import sys
input = sys.stdin.readline
lst = sorted([[*map(int, input().split())] for _ in range(int(input()))], key=lambda x:-x[1])
ans=ra=0
for x,y in lst:
    if ra < x:
        ans += (x-ra) * y
        ra = x
print(ans)

# 접근 1
# 대충 일단 한 사분면만 생각해보자
# 층을 나눠서 볼 수 있지 않을까?
# 대충 모양은 피라미드처럼 깎아내리는 모양이 될 것
# dict로 필요한 값만 담으면서 뭔가 for문 돌려보자
# -> 제대로 구현 안 됨

# 접근 2
# 일단 x축 기준으로 정렬하자
# 순회를 돌면서 x축, y축의 높이를 저장하는 두 배열을 넓혀나가자
# 만약 더 높은 y축이 나오는 순간, 배열에서 그보다 작은 y축들은 전부 무시된다.
# 그럼 걔네는 pop시키면 되겠다 (like stack)
# 순회 다 돌면 두 배열을 곱하면서 정답을 만들면 되겠다
# -> 시간 초과

# 접근 3
# y축 기준으로 내림차순 정렬하자
# 높은 y축을 가지고 있는 놈의 넓이 값은 절대 무시되지 않는다.
# 그러면 그보다 작은 y 축이 가지는 넓이값은 언제 무시되지 않는가?
# x축 쪽으로 조금 더 길 때!
# 순회를 돌면서 y축이 점차 작은 놈들이 나올 텐데 이놈들의 x값을 따져서 튀어나온 녀석들만
# 값을 곱하자
# -> 통과
