# 세금
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
S, D = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(M)]
increase = [int(input()) for _ in range(K)]


