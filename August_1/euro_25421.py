# 25421번: 조건에 맞는 정수의 개수
# https://www.acmicpc.net/problem/25421

import sys

n = int(sys.stdin.readline().rstrip())

def count(num):
    digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if num == 1:
        return digit
    else:
        result = []
        for num in count(num-1):
            last = num % 10
            for d in digit:
                if (abs(last - d) <= 2):
                    result.append(num * 10 + d)
        return result

print(len(count(n)))