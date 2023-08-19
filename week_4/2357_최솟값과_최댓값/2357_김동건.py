# 2357 최솟값과 최댓값 (G1)
# https://www.acmicpc.net/problem/2357
# 정답

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
lst = [int(input()) for _ in range(n)]

size = 1
while size <= n: size<<=1
size<<=1
st=[0,0]*size

def init(i,s,e):
    if s==e:
        st[i]=[lst[s],lst[s]]
        return st[i]
    m=(s+e)>>1
    nn=i<<1
    lmin,lmax=init(nn,s,m)
    rmin,rmax=init(nn+1,m+1,e)
    st[i]=[min(lmin,rmin),max(lmax,rmax)]
    return st[i]

def search(i,s,e,a,b):
    if e<a or b<s: return (sys.maxsize,0)
    if e<=b  and a<=s: return st[i]
    m=(s+e)>>1
    nn=i<<1
    lmin,lmax=search(nn,s,m,a,b)
    rmin,rmax=search(nn+1,m+1,e,a,b)
    return (min(lmin,rmin),max(lmax,rmax))

init(1,0,n-1)
for _ in range(m):
    a,b=map(int,input().split())
    print(*search(1,0,n-1,a-1,b-1))

# 세그먼트 트리 복습 문제.
# 세그먼트 트리가 가지는 중요한 포인트는 배열을 트리화시켰을 때 부모 노드가 자식 노드에서 추출된 정보를 가진다는 것.
# 구간합에 사용할 수도 있지만, 최대값, 최소값을 저장하는데 사용할 수도 있다.

# 해당 문제는 구간 내에서의 최대와 최소를 여러번에 걸쳐 구할 것을 요구한다.
# n,m이 10만이며 정렬도 할 수 없기 때문에 최대로는 10만 * 10만의 시간복잡도를 가질 수도 있다.
# 이를 줄이기 위해 세그먼트 트리를 구성한다.
# nlogn으로 트리를 구성하고 대체로 logn * 2의 시간을 들여 최대 최소를 구할 수 있다.
# nlogn + mlogn의 시간 복잡도를 가질 것으로 생각됨

# 접근 1
# 일단 세그먼트 트리 간단 구현 연습.
# 최대 최소 담는 세그먼트 트리 배열 따로 선언
# 접근 2
# 둘을 한꺼번에 담는 배열 만들기