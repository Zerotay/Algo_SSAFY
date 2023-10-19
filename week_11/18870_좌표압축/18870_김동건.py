# 18870 좌표 압축 (S2)
# https://www.acmicpc.net/problem/18870
# 정답

import sys

input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split(" ")))
sortlst = sorted(set(lst))
dic = {sortlst[i]: i for i in range(len(sortlst))}
for i in lst:
    print(dic[i], end=" ")

# 최소값이 0이면 되는 순서값 구하기 문제
# 정렬해서 각 자리값을 인덱스로 치환
# 그리고 각 자리값에 맞춰서 인덱스 값을 구한다.
