# 2533 사회망 서비스(SNS)
# https://www.acmicpc.net/problem/2533

from sys import stdin

N = int(stdin.readline())
arr = [[] for i in range(N+1)]
print(arr)

global even
even = []
global odd
odd = []

for i in range(N-1):
    u, v = map(int, stdin.readline().split())
    arr[u].append(v)






def bfs(idx_arr, depth):
    global odd
    global even
    if (depth % 2 == 0):
        even += idx_arr
    else:
        odd += idx_arr
    new = []
    for idx in idx_arr:
        new += arr[idx]
    
    if (len(new) != 0):
      bfs(new, depth+1)


bfs([1], 1)
print(odd)
print(even)

print(min(len(odd), len(even)))
