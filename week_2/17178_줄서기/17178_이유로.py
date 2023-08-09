# 17178 줄서기 (G5)
# https://www.acmicpc.net/problem/17178
# 실패

import sys
input = sys.stdin.readline

N = int(input())

arr = []

for i in range(N):
    arr.append(input().split())

flatten = []
for row in  arr:
    flatten.extend(row)

sortedFlatten = sorted(flatten, key=lambda x: (x.split("-")[0], x.split("-")[1]))

stack = []
count = 0
answer = len(flatten)

while len(flatten) > 0:
    while len(stack) > 0 and stack[-1] == sortedFlatten[count]:
            stack.pop()
            count += 1

    if flatten[0] == sortedFlatten[count]:
        count += 1
    else:
        stack.append(flatten[0])
    flatten = flatten[1:]

while len(stack) > 0 and stack[-1] == sortedFlatten[count]:
        stack.pop()
        count += 1


if count == answer:
    print("GOOD")
else:
    print("BAD")
