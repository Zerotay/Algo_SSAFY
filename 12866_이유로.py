import sys
input = sys.stdin.readline

N = int(input())
text = input()

a = 0
c = 0
g = 0
t = 0

for i in [*text]:
    if i == 'A':
        a += 1
    
    if i == 'C':
        c += 1
    
    if i == 'G':
        g += 1
    
    if i == 'T':
        t += 1

print(a*c*g*t)
    