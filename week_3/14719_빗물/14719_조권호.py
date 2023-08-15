h,w = map(int,input().split())
block = list(map(int,input().split()))

ans=0
ptr=0
stk=[]
for i in range(1, w):
    if block[i]>=block[ptr]:
        while stk:
            ans+=block[ptr]-stk.pop()
        ptr = i
    else:
        stk.append(block[i])
if stk:
    max_stk = max(stk)
    for s in stk:
        ans+=max_stk-s
print(ans)