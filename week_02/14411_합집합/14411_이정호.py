import sys
input = sys.stdin.readline

n = int(input())
rectangles = []
for _ in range(n):
    rectangles.append(list(map(int, input().split())))  # 오름차순의 역순으로 정렬

# print(rectangles)
rectangles.sort(key=lambda x: -x[1]) 
# print(rectangles)
ans = 0
x = 0
for rectangle in rectangles:
    if rectangle[0] > x:
        ans += (rectangle[0] - x) * rectangle[1]
        x = rectangle[0]
print(ans)