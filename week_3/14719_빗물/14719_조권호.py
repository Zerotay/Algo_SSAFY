h,w = map(int,input().split())
block = list(map(int,input().split()))

ans=0
ptr1=0
ptr2 = w-1
left = block[ptr1]
right = block[ptr2]

while ptr1<=ptr2:
    left = max(left, block[ptr1])
    right = max(right, block[ptr2])

    if left<=right:
        ans += left - block[ptr1]
        ptr1+=1
    else:
        ans += right - block[ptr2]
        ptr2-=1
print(ans)
