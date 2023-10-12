# 9935 문자열 폭발(G4)
# https://www.acmicpc.net/problem/9935
# 정답

import sys
input = sys.stdin.readline

'''
시간초과 => 문자열 슬라이싱이 O(N) 소모
str = input().rstrip()
bomb = input().rstrip()
str_len = len(str)
bomb_len = len(bomb)
for i in range(str_len,-1,-1):
    if(i+bomb_len>=len(str)):
        continue
    if str[i:i+bomb_len]==bomb:
        str = str[:i]+str[i+bomb_len:]
if len(str)==0:
    print("FRULA")
else:
    print(str)
'''
str = input().rstrip()
bomb = input().rstrip()
bomb_len = len(bomb)
stk =[]

for i in str:
    stk.append(i)
    if len(stk)>=bomb_len:
        if stk[-bomb_len:] == list(bomb):
            for _ in range(bomb_len):
                stk.pop()
if len(stk)==0:
    print("FRULA")
else:
    print(*stk, sep='')