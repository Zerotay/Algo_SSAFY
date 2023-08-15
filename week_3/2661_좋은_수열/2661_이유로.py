# 2661 좋은 수열 (G4)
# https://www.acmicpc.net/problem/2661
# 오답

import sys
input = sys.stdin.readline

n = int(input())

def good(n):
    if (n == 1):
        return '1'
    previous = good(n-1)
   
    for i in range(1, 4):
        flag = True
        if previous[-1] == str(i):
            flag = False
        for j in range(1, int(n/2)):
            # print(previous[n-2-j*2:n-1-j], (previous[n-1-j:] + str(i)))
            if (previous[n-2-j*2:n-1-j] == previous[n-1-j:] + str(i)):
                flag = False
        if flag:
            return previous + str(i)
    
    return previous

print(good(n))
        

