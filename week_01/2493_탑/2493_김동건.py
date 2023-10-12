n = int(input())
inlst = [*map(int, input().split())]
lst = []
for i, val in enumerate(inlst):
    while lst and lst[-1][0] < val: lst.pop()
    print(0 if not lst else lst[-1][1], end=' ')
    lst.append((val, i+1))
