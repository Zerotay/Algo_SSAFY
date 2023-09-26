# 27172 수 나누기 게임(G5)
# https://www.acmicpc.net/problem/27172
# 정답

n = int(input())
lst = [*map(int, input().split())]
maxSize = 1000001
checkLst = [0] * maxSize
isExist = [False] * maxSize
for i in lst:
    isExist[i] = True

for i in lst:
    for j in range(i * 2, maxSize, i):
        if isExist[j]:
            checkLst[i] += 1
            checkLst[j] -= 1

print(*(checkLst[i] for i in lst))

# 접근 1
# 그냥 모든 조합 고려해보자. -> 시간 초과

# 접근 2
# 에라토스테네스의 체 만들듯이 위로 진행시켜가면서 있는 값에 대해서만 체크하자
# 성공
