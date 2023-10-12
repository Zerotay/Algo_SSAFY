import sys
input = sys.stdin.readline


n= int(input())
limit = list(map(int,input().split()))

m= int(input())
boxes = list(map(int,input().split()))

limit.sort(reverse = True)
boxes.sort(reverse = True)

if limit[0]< boxes[0]:
    print(-1)
    exit(0)
cnt =0
while(boxes):
    for i in range(len(limit)):
        if boxes and limit[i] < boxes[-1]:
            continue
        for j in range(len(boxes)):
            if( limit[i] >= boxes[j]):
                boxes.remove(boxes[j])
                break
    cnt+=1
print(cnt)
