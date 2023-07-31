n = int(input())
di = 987654321

num = [[1,1,1,1,1,1,1,1,1],[3,4,5,5,5,5,5,4,3]]
for i in range(n-1):
    tmp = []
    for i in range(9):
        if i==0:
            tmp.append((num[-1][i]+num[-1][i+1]+num[-1][i+2])%di)
        elif i==1:
            tmp.append((num[-1][i-1]+num[-1][i]+num[-1][i+1]+num[-1][i+2])%di)
        elif i==7:
            tmp.append((num[-1][i-2]+num[-1][i-1]+num[-1][i]+num[-1][i+1])%di)
        elif i==8:
            tmp.append((num[-1][i-2]+num[-1][i-1]+num[-1][i])%di)
        else:
            tmp.append((num[-1][i-2]+num[-1][i-1]+num[-1][i]+num[-1][i+1]+num[-1][i+2])%di)
    num.append(tmp)
print(sum(num[n-1])%di)