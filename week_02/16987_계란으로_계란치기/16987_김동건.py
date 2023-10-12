# 16987 계란으로 계란치기 (G5)
# https://www.acmicpc.net/problem/16987
# 정답

n = int(input())
inlst = [[*map(int, input().split())] for _ in range(n)]
ans = 0
eggs = [*map(lambda x: x[0], inlst)]

def recur(count, eggs):
    if not any(eggs):
        print(n)
        exit(0)
    if count == n:
        global ans
        ans = max(ans, len([*filter(lambda x :not x, eggs)]))
        return
    if not eggs[count]:
        recur(count+1, eggs)
        return
    for i in range(n):
        if i == count: continue
        if not eggs[i]:
            recur(count+1, eggs)
            continue
        tmp = eggs[:]
        tmp[count] = eggs[count] - inlst[i][1] if eggs[count] > inlst[i][1] else 0
        tmp[i] = eggs[i] - inlst[count][1] if eggs[i] > inlst[count][1] else 0
        recur(count+1, tmp)


recur(0, eggs)
print(ans)

# 접근 1
# 백준에서 입력이 8개? 무조건 완탐
# 문제 이해가 조금 어렵다
# 일단 계란 하나를 드는 작업을 한다. 이건 순서대로
# 대신 어따가 찍을 지는 자유! 여기에서 경우의 수가 발생한다
# 다 깨졌거나 마지막의 계란을 들었다면 종료.
# 이해했다면 문제에 맞게 구현만 하면 된다.
# 재귀를 돌면서 계란들의 체력을 담는 리스트를 같이 넣었다.
# -> 성공