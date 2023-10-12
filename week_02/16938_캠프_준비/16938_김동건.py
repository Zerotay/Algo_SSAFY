# 16938 캠프 준비 (G5)
# https://www.acmicpc.net/problem/16938
# 정답

import itertools as t
n,l,r,x = map(int,input().split())
lst = [*map(int,input().split())]
print(sum(1 for i in range(2,n+1) for j in t.combinations(lst,i) if l<=sum(j)<=r and max(j)-min(j)>=x))

# 접근 1
# 조합인데 조건 따지는 조합이다
# 파이썬의 무기를 잘 활용해보자
# -> 성공