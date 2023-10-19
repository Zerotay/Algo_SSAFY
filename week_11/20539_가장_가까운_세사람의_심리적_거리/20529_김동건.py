# 20529 가장 가까운 세 사람의 심리적 거리 (S1)
# https://www.acmicpc.net/problem/20529
# 정답

import sys
from collections import Counter
from itertools import combinations as cb
import functools
input = sys.stdin.readline
mbti = ["INFP","INFJ","INTP","INTJ","ISFP","ISFJ","ISTP","ISTJ","ENFP","ENFJ","ENTP","ENTJ","ESFP","ESFJ","ESTP","ESTJ"]
mbtiToBit = {j:i for i,j in enumerate(mbti)}

@functools.cache
def com(a:int, b:int)->int: 
    return int(a ^ b).bit_count()

for _ in range(int(input())):
    n = int(input())
    lst = list(map(lambda x: mbtiToBit[x], input().rstrip().split()))
    if Counter(lst).most_common(1)[0][1] > 2: print(0)
    else:
        ans = sys.maxsize
        for a, b, c in cb(lst, 3): ans = min(ans, com(a,b)+com(b,c)+com(c,a))
        print(ans)

# 비둘기집의 원리
# 비둘기집이 n개 있고 그보다 비둘기 수가 많다면,
# 어떤 조합으로 비둘기를 집에 넣더라도 어떤 비둘기집에는 비둘기가 2마리 이상 들어가게 된다

# 거리는 비트 연산으로
# 어차피 종류는 16가지니까 중복 제거를 하는 방향으로 간다
# 어느 mbti가 3명 있으면 답은 0
# 그 외의 경우 최대 사람이 48명 있다는 뜻이므로
# 그냥 조합을 걸어서 답을 구한다