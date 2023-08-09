# 16638 괄호 추가하기 2 (G1)
# https://www.acmicpc.net/problem/16638
# 

import sys
input = sys.stdin.readline

N = int(input())

text = input()
idx = []

for i in range(N):
    if (text[i] == '+' or text[i] =='-'):
        idx.append(i)

R = len(idx)

isSelected = [False] * R
max = -sys.maxsize - 1

def subset(cnt):
    global max
    if cnt == R:
        try :
            for i in range(R):
                if isSelected[i]:
                    updatedText = text[:idx[i]-1] + "(" + text[idx[i]-1:idx[i]+2] + ")" + text[idx[i]+2:]
                    result = eval(updatedText)
                    if max < result:
                        max = result
        except:
            return
        return

    isSelected[cnt] = True
    subset(cnt+1)
    isSelected[cnt] = False
    subset(cnt+1)


subset(0)

print(max)