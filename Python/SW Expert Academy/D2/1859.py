T = int(input())

for tc in range(T):
    N = int(input())
    prices = [int(i) for i in input().split()]

    max_price = prices[-1]
    result = 0

    for i in range(len(prices)-1, -1, -1):  # 뒤에서부터 계산
        price = prices[i]
                
        if max_price < price:
            max_price = price
            
        result += max_price - price
        
    print(f'#{tc + 1} {result}')


## 앞으로 풀다가 RuntimeError발생한 코드, 로직은 맞지만 시간이 오래 걸리는 듯
# for i in range(len(prices)):
#         cal_lst.append(prices[i])
        
#         if max_price == 0:
#             max_price = prices[i]

#         if (max_price < prices[i]) and prices[i] == max(prices[i:]):
#             result += (prices[i] * len(cal_lst)) - sum(cal_lst)
#             max_price = 0
#             cal_lst.clear() 
        
#     print(f'#{tc + 1} {result}')



