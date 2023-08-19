# 2225 합분해 (G5)
# https://www.acmicpc.net/problem/2225
# 정답


n,k=map(int,input().split())
m=10**9
dp=[[0]*k for _ in range(n+k)]

def recur(a,b):
    if dp[a][b]: return dp[a][b]
    if b in[a,0]:
        dp[a][b]=1
        return dp[a][b]
    dp[a][b]=(recur(a-1,b-1)%m+recur(a-1,b)%m)%m
    return dp[a][b]

print(recur(n+k-1,k-1))

# print(len([*cr([i for i in range(k)],n)]) % m)
# print(len([*cb([i for i in range(n+k-1)], k-1)]) % m)

# import math
# n,k=map(int,input().split())
# print(math.comb(n+k-1,n)%10**9)


# 19 20 21 / 3!
# n+k-1 C k-1

# 접근 1
# 중복조합 문제
# k개에서 중복 가능으로 n개 뽑기
# 파이썬의 훌륭한 함수를 사용해본다
# -> 메모리 초과

# 접근 2
# 중복 조합인 걸 알았으면 조합으로 환산한다.
# 줄 세워두고 자를 자리 고르는 문제
# 조합으로 환산해도 결국 파이썬 함수는 사용 못 할 것 같다
# 조합을 분할한다.
# 파스칼의 삼각형을 이용한다.
# 중복 방지를 위해 dp도 활용한다
# -> 성공

# n,k는 최대 20이므로 공간은 널널하다

# 접근 3
# 다른 사람 풀이 보다가 알게 됐는데
# 훌륭한 파이썬 math라이브러리에 comb가 있다
# 심지어 이게 실행속도도 더 빠르다..
