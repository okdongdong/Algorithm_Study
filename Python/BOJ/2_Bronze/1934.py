import sys
input = sys.stdin.readline


def gcd(a, b):
    a, b = sorted((a, b))
    while b:
        a, b = b, a % b

    return a


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A*B//gcd(A, B))
