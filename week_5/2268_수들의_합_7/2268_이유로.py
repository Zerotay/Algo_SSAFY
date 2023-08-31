# 2268 수들의 합 7 (G1)
# https://www.acmicpc.net/problem/2268
# 시간초과

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]*n
tree = [0]*(n*4)
commands = [[*map(int, input().split())] for _ in range(m)]

# def init(node, start, end):
#   global tree, arr
#   if (node > 100):
#     return
#   if start == end:
#       tree[node] = arr[start]
#       return tree[node]
#   else:
#      mid = int((start+end)/2)
#      nn = node * 2
#      tree[node] = init(nn, start, mid) + init(nn+1, mid+1, end)
#      return tree[node]

def sum(node, start, end, left, right):
  global tree, arr
  if left > end or right < start:
    return 0
  if left <= start and end <= right:
     return tree[node]
  
  mid = int((start + end) / 2)
  nn = node * 2

  return sum(nn, start, mid, left, right) + sum(nn+1, mid+1, end, left, right)

def update(node, start, end, index, diff):
   global tree, arr
   if index < start or index > end:
      return
   
   tree[node] += diff

   if start == end:
      arr[index] = tree[node]
      return
   
   mid = int((start + end) / 2)
   nn = node * 2
   update(nn, start, mid, index, diff)
   update(nn+1, mid+1, end, index, diff)




for c in commands:
   if c[0] == 0:
      if c[1] <= c[2]:
        print(sum(1, 0, n-1, c[1]-1, c[2]-1))
      else:
         print(sum(1, 0, n-1, c[2]-1, c[1]-1))
   elif c[0] == 1:
      if c[1] <= c[2]:
        diff = c[2] - arr[c[1]-1]
        update(1, 0, n-1, c[1]-1, diff)
      else:
        diff = c[1] - arr[c[2]-1]
        update(1, 0, n-1, c[2]-1, diff)