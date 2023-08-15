# 2661 좋은 수열 (G4)
# https://www.acmicpc.net/problem/2661
# 시간초과

import sys
input = sys.stdin.readline

n = int(input())

def good(n):
    digit = ['1', '2', '3']

    if (n == 1):
        return digit
    
    previousArr = good(n-1)
    resultArr = []

    for previous in previousArr:
        for i in digit:
            flag = True
            if previous[-1] == str(i):
                flag = False
            for j in range(1, int(n/2)):
                # print(previous[n-2-j*2:n-1-j], (previous[n-1-j:] + str(i)))
                if (previous[n-2-j*2:n-1-j] == previous[n-1-j:] + str(i)):
                    flag = False
            if flag:
                resultArr.append(previous + str(i))
    
    return resultArr

print(good(n)[0])
        

