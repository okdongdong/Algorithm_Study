# 숫자 카드 2
N = int(input())
temp = input().split()
my_cards = dict()
for card in temp:
    try:
        my_cards[card] += 1
    except:
        my_cards[card] = 1

M = int(input())
cards = input().split()
result = []
for card in cards:
    temp = my_cards.get(card)
    if temp:
        result.append(str(temp))
    else: 
        result.append('0')

print(' '.join(result))