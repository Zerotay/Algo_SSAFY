# 28709 와일드카드 괄호 문자열 (G1)
# https://www.acmicpc.net/problem/28709
# 실패

import sys
from collections import deque
input=sys.stdin.readline

t = int(input())

def removeQuestion(lines):
    
    replaced = []
    result = []
    for line in lines:
        if '?' in line:
            replaced.append(line.replace('?', '('))
            replaced.append(line.replace('?', ')'))
        else:
            replaced.append(line)

    return list

def get(target):
    stack = deque([])
    for i in range(len(target)):

        if len(stack) == 0:
            stack.append(target[i])
        else:
            last = stack.pop()
            if target[i] == '(':
                stack.append(last)
                stack.append(target[i])
            elif target[i] == ')':
                if last == ')':
                    stack.append(last)
                    stack.append(target[i])
                elif last == '*':
                    stack.append(last)
            # elif target[i] == '?':
            #     if last == ')':
            #         stack.append(last)
            #         stack.append(target[i])
            #     elif last == '*':
            #         stack.append(last)
            #     elif last == '?':
            #         stack.append(last)
            #         stack.append(target[i])
            elif target[i] == '*':
                while(last != ')' and len(stack) > 0):
                    last = stack.pop()
                if last == ')':
                    stack.append(last)    
                stack.append('*')
    print(stack)
            
    if ('(' in stack or ')' in stack):
        return 0
    elif len(stack) % 2 == 1 and '?' in stack:
        return 0
    else:
        return 1

answers = []
for _ in range(t):
    
    line = input().rstrip()
    arr = []
    arr.append(line)
    print(removeQuestion(arr))
    # results = []
    # reversedLine = ""
    # for i in range(len(line)):
    #     if line[i] == '(':
    #         reversedLine =  ")" + reversedLine
    #     elif line[i] == ')':
    #         reversedLine =  "(" + reversedLine
    #     else:
    #         reversedLine =  line[i] + reversedLine

    # results.append(get(line))
    # results.append(get(reversedLine))

    # if (1 in results):
    #     answers.append("YES")
    # else:
    #     answers.append("NO")

for answer in answers:
    print(answer)