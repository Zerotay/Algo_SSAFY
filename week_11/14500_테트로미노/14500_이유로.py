# 14500 테트로미노 (G4)
# https://www.acmicpc.net/problem/14500
# 실패

import sys

input = sys.stdin.readline


n, m = map(int, input().split())
arr = []
for i in range(n):
  arr.append([*map(int, input().split())])
  
answer = 0

for i in range(n):
  for j in range(m-3):
    answer = max(answer, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3])
    
for i in range(n-1):
  for j in range(m-1):
    answer = max(answer, arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1])
    
for i in range(n-2):
  for j in range(m-1):
    answer = max(answer, arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1])
    
for i in range(n-2):
  for j in range(m-1):
    answer = max(answer, arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1])
    
for i in range(n-1):
  for j in range(m-2):
    answer = max(answer, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1])
    
print(answer)