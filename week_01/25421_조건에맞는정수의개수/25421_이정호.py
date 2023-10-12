import sys
input = sys.stdin.readline

n = int(input())
mod = 987654321

num = [[1,1,1,1,1,1,1,1,1],[3,4,5,5,5,5,5,4,3]]
for i in range(n-1):
    tmp = []
    for i in range(9):
        if i==0:
            tmp.append((num[-1][i]+num[-1][i+1]+num[-1][i+2])%mod)
        elif i==1:
            tmp.append((num[-1][i-1]+num[-1][i]+num[-1][i+1]+num[-1][i+2])%mod)
        elif i==7:
            tmp.append((num[-1][i-2]+num[-1][i-1]+num[-1][i]+num[-1][i+1])%mod)
        elif i==8:
            tmp.append((num[-1][i-2]+num[-1][i-1]+num[-1][i])%mod)
        else:
            tmp.append((num[-1][i-2]+num[-1][i-1]+num[-1][i]+num[-1][i+1]+num[-1][i+2])%mod)
    num.append(tmp)
print(sum(num[n-1])%mod)