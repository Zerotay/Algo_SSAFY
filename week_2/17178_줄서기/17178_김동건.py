# 17178 줄서기 (G5)
# https://www.acmicpc.net/problem/17178
# 정답

inlst = []
for _ in range(int(input())):
    inlst.extend([*map(lambda x: [x[0], int(x[1])], map(lambda x: x.split('-'), input().split()))])

inlst.reverse()
best = [*reversed(sorted(inlst))]
stack = []
while inlst:
    tmp = inlst.pop()
    if tmp == best[-1]:
        best.pop()
        continue
    while stack and stack[-1] == best[-1]:
        stack.pop()
        best.pop()
    if stack and stack[-1] < tmp:
        print("BAD")
        exit()
    stack.append(tmp)

print("GOOD")

# 접근 1
# 개단순한 스택 문제다
# 근데 정렬이 조금 어려운..
# 5명씩 서고 이런 건 의미 없다.
# 스택에 값을 넣을 때 순서가 바뀌어서 들어가는 순간이 있는지만 확인하자
# 달리 말하면 스택에 들어갈 때부터 정렬된 상태로 들어가야 한다는 것이다
# 또, 입장 순서는 정해져있으니 그것을 나타내는 리스트가 필요하겠다
# -> 성공