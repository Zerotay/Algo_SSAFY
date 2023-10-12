n = input()
arr = list(map(int,input().split()))

ans =[0]
stk =[(arr[0],0)]

for i in range(1, len(arr)):
    if(arr[i]>arr[i-1]):
        while True:
            if len(stk)==0 or stk[-1][0]>arr[i]:
                break
            stk.pop()
    stk.append((arr[i],i))
    if(len(stk)>1):
        ans.append(stk[-2][1]+1)
    else:
        ans.append(0)
print(*ans)