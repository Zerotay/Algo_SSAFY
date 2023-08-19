import sys
input=sys.stdin.readline


for _ in range(int(input())):
    string=input().rstrip()
    l = 0
    while l!=len(string):
        l = len(string)
        string=string.replace('()','')
    print(string)
    # print(string.replace('()',''))