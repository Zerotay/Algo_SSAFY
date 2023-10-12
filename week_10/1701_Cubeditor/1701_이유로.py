# 1701 Cubeditor (G3)
# https://www.acmicpc.net/problem/1701
# 시간초과

import sys
input = sys.stdin.readline

line = input().rstrip()

for c in range(len(line)-1, 0, -1):
  for s in range(len(line)-c):
    pattern = line[s:s+c]

    tlen = len(line)
    plen = len(pattern)

    p = [0] * plen

    j=0
    for i in range(1, plen):
      while j>0 and pattern[i] != pattern[j]:
        j = p[j-1]
      
      if pattern[i] == pattern[j]:
        j += 1
        p[i] = j
        

    cnt = 0
    list = []
    j=0
    for i in range(tlen):
      while j > 0 and line[i] != pattern[j]:
        j = p[j-1]
      if line[i] == pattern[j]:
        if j == plen-1:
          cnt += 1
          list.append(i-plen+1)
          j = p[j]
        else:
          j += 1
    if cnt > 2:
      print(c)
      exit(0)

