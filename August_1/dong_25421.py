n=int(input())
m=987654321
lst = [[1]*9 for _ in range(n+1)]
for i in range(2, n+1):
    lst[i][0] = (lst[i-1][0]+lst[i-1][1]+lst[i-1][2]) % m
    lst[i][1] = (lst[i-1][0]+lst[i-1][1]+lst[i-1][2]+lst[i-1][3]) % m
    for j in range(2, 7):
        lst[i][j] = (lst[i-1][j-2]+lst[i-1][j-1]+lst[i-1][j]+lst[i-1][j+1]+lst[i-1][j+2]) % m
    lst[i][7] = (lst[i-1][5]+lst[i-1][6]+lst[i-1][7]+lst[i-1][8]) % m
    lst[i][8] = (lst[i-1][6]+lst[i-1][7]+lst[i-1][8]) % m

print(sum(lst[n]) %m)
