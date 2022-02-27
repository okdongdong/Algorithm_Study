# 카드
import sys
input = sys.stdin.readline
N = int(input())
cards = dict()
for _ in range(N):
    temp = int(input())
    try:
        cards[temp] += 1

    except:
        cards[temp] = 1

max_cnt, max_num = 0, 0
for num, cnt in cards.items():
    if cnt > max_cnt:
        max_cnt = cnt
        max_num = num
    
    elif cnt == max_cnt:
        if max_num > num:
            max_num = num

print(max_num)