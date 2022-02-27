# 3499. 퍼펙트 셔플

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(input().split())
    result = []
    
    card1 = cards[:(N+1)//2]    # 카드뭉치를 반으로 나눔
    card2 = cards[(N+1)//2:]    # N이 짝수면 각각의 길이는 (N+1)//2로 동일, 홀수면 card1이 1큼
    

    for i in range(0, N//2):    # 반으로 나눈 길이만큼 반복
        result.append(card1[i]) # 각각의 카드뭉치에서 카드 값을 하나씩 넣어줌 
        result.append(card2[i])

    if N%2:                     # N이 홀수일 경우 card1이 하나 더 많으므로 마지막에 추가해줌
        result.append(card1[-1]) 
        

    print('#{}'.format(tc), *result)