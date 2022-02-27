N, C, W = map(int, input().split())
woods = [int(input()) for _ in range(N)]

max_money = 0
max_l = max(woods)

for l in range(1, max_l + 1):       # l : 정제된 나무의 길이
    profit_sum = 0
    
    for wood in woods:       
        q, r = divmod(wood, l)      # 몫 : 나무토막의 수, 나머지 : 자투리 부분 
        
        if r:
            expense = q * C         # 자투리가 있을 경우 자투리 손질로 횟수 1회 추가
        else:
            expense = (q - 1) * C   # 자투리 없이 딱 잘라질 경우
        profit = (q * l * W) - expense
        
        if profit < 0:              # 나무를 잘랐을 때 손실이 난다면 그 나무는 버림
            continue 

        profit_sum += profit
        
    if profit_sum >= max_money:
        max_money = profit_sum
            
print(max_money)
