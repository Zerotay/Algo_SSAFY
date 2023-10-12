# 28709 와일드카드 괄호 문자열 (G1)
# https://www.acmicpc.net/problem/28709
# 정답

import sys
input=sys.stdin.readline

for _ in range(int(input())):
    string=input().rstrip()
    wild=flag=0

    lqm=lcnt=0
    for i in string:
        if i=='(':lcnt+=1
        elif i==')':lcnt-=1
        elif i=='?':lqm+=1
        else:break

        if lcnt < 0:
            if lqm + lcnt < 0:
                flag=1
                break
            lqm+=lcnt
            lcnt=0
    if flag:
        print('NO')
        continue

    rqm=rcnt=0
    for i in reversed(string):
        if i=='(':rcnt-=1
        elif i==')':rcnt+=1
        elif i=='?':rqm+=1
        elif i=='*':
            wild=1
            break

        if rcnt < 0:
            if rqm+rcnt<0:
                flag=1
                break
            rqm+=rcnt
            rcnt=0
    if wild:
        print('YES')
        continue
    if flag or ((rqm+rcnt)%2 and (lqm+lcnt)%2):
        print('NO')
        continue
    print("YES")

# 접근 1
# replace로 날먹 가능한 경우가 더러 있으니 일단 .replace('()','') 때려둠
# ?가 나올 때마다 스택에 담는다.
# *가 나오면 거의 웬만한 문제가 해결되니까 스택을 초기화한다.
# 앞으로 전진하면서 괄호가 열고 닫히는 것을 체크한다.
# 괄호가 과도하게 열려있는 상태라면 이후 등장하는 값에 따라 미정이지만
# 괄호가 과도하게 닫혀있는 상태라면 ?나 *로 해결할 수 있는 케이스인지 살펴야 한다.
# -> 구현 실패

# 접근 2
# 한쪽으로 쭉 직진하면서 제때에 괄호가 닫히는지만 체크하면 된다는 아이디어는 좋다
# 생각해보니 *가 등장하기만 하면 만사가 해결된다.
# 대신 *의 영향을 받지 않는 영역에 대해서만 체크를 해주면 완벽하다
# 그러면 앞쪽에서 쭉 봤듯이 뒤쪽에서도 쭉 봐주면 되겠다
# 그러면 스택에는 ?만 담기는 거니까 스택을 쓸 필요도 사실 없다
# 한쪽으로 진행하면서 음수가 생기는 시점에 모아둔 ?를 털자
# -> 예외 케이스 발생

# 접근 3
# 양 끝으로 문제가 없는 상태에서 한번이라도 *가 나왔으면 무조건 yes
# 양쪽에서 진행하고 남은 찌끄레기들을 살펴본다.
# 열린 값만큼 ?가 존재해준다면, 그리고 남은 ?가 짝수개라면 성공이다.
# -> 성공

# 문자열의 최대 길이는 50만. 테스트케이스가 10000개여도 결국 총 길이는 50만.
# 한쪽으로 진행하면서 탐색을 해도, 그걸 거꾸로 다시 탐색해도 끽해야 결국 100만번 탐색이다.



# 가면서 cnt )면 - (면 + 갑자기 -되면 노
# +면 뒤의 누군가가 해결해줄거다
# -면 앞에서 해결할 전략이 있었는지 봐야한다
# (()?)    )
# ()*???***()))
#??))
# *?)
# ?*)
# *가 해결 못해주는 사례가 있나
# *
# (((???
# 뒤 때문에 안되는 케이스
# ?(
# *(
#
# ((?())
# ?((())
# ?(((?())
# ?)(?
