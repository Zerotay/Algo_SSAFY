inlst = input()
bomb = input()
len_bomb = len(bomb)
ans = []

for i in inlst:
    ans.append(i)
    if "".join(ans[-len_bomb:]) == bomb:
        del ans[-len_bomb:]

print("".join(ans) if ans else "FRULA")
