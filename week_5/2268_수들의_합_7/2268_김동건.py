import sys
input = sys.stdin.readline
n,m = map(int, input().split())

size = 1
while size<n:
    size<<=1
size<<=1
seg = [0]*size
lst = [0] * (n+1)

# def init(node, left, right):
#     if left == right:
#         seg[node] = 0
#         return seg[node]
#     mid = (left + right)//2
#     nn = node **2
#     seg[node] = init(nn, left, mid) + init(nn+1, mid+1, right)
#     return seg[node]

def search(node, s, e, l, r):
    if r < s or l > e:
        return 0
    if l <= s and e <= r:
        return seg[node]
    mid = (s+e)//2
    nn = node * 2
    return search(nn, s, mid, l, r) + search(nn+1, mid+1, e, l, r)

def update(node , left, right, what, val):
    if left > what or right < what:
        return seg[node]
    seg[node] += val
    if left == right:
        lst[left]+=val
        return
    mid = (left+right)//2
    nn = node * 2
    update(nn, left, mid, what, val)
    update(nn+1, mid+1, right, what, val)

# init(1, 0, n-1)
# print(size)
for _ in range(m):
    a,b,c = map(int, input().split())
    
    if a:
        t=c-lst[b-1]
        # t = c
        update(1, 0, n-1, b-1,t)
        # print(seg)
    else:
        if b>c: b,c = c,b
        print(search(1,0,n-1,b-1,c-1))