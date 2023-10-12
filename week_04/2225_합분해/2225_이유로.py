# 2225 합분해 (G5)
# https://www.acmicpc.net/problem/2225
# 시간초과

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
count = 0

def add(line, cnt):
    global n, k, count
    result = eval(line)
    if (result > n or cnt > k):
        return
    
    if cnt <= k and result == n:
        count += 1
        return
    
    for i in range(0, n+1):
        add(line + "+" + str(i), cnt+1)
        
add("0", 0)

print(count)