# 28709 와일드카드 괄호 문자열 (G1)
# https://www.acmicpc.net/problem/28709
# 실패

import sys
from collections import deque
input=sys.stdin.readline

t = int(input())

for _ in range(t):
    stack = deque([])
    line = input()

    for i in range(len(line)):
        if line[i] == '(':
            stack.append(line[i])
        elif line[i] == ')':
            if len(stack) > 0:
                last = stack.pop()
                if last == ')':
                    stack.append(last)
                    stack.append(line[i])
                elif last == '*':
                    stack.append(last)
            else:
                stack.append(line[i])
        elif line[i] == '?':
            if len(stack) > 0:
                last = stack.pop()
                if last == ')':
                    stack.append(last)
                    stack.append(line[i])
                elif last == '*':
                    stack.append(last)
                elif last == '?':
                    stack.append(last)
                    stack.append(line[i])
            else:
                stack.append(line[i])
        elif line[i] == '*':
            if len(stack) > 0:
                last = stack.pop()
                while(last != ')' and len(stack) > 0):
                    last = stack.pop()
                if last == ')':
                    stack.append(last)        
                stack.append('*')
            else:
                stack.append('*')

        # print(stack)
            
    if (len(stack) == 0):
        print("YES")
    elif (len(stack) == 1 and '*' == stack.pop()):
        print("YES")
    else:
        print("NO")
