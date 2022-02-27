# 단어 정렬
import sys
input = sys.stdin.readline
N = int(input())
words = [input() for _ in range(N)]
words = list(set(words))
words.sort(key=lambda x:(len(x),x))
print(*words, sep='')