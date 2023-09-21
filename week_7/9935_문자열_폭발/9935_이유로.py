# 9935 문자열 폭발 (G4)
# https://www.acmicpc.net/problem/9935
# 정답

import sys
input = sys.stdin.readline

line = input().rstrip()
s = input().rstrip()

stack = []
l = len(s)

for i in range(len(line)):
    stack.append(line[i])
    if ''.join(stack[-l:]) == s:
        for _ in range(l):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')