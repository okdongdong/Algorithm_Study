T = int(input())
for i in range(T):
    P, Q, R, S, W = map(int, input().split())
    
    A_price = P * W
    B_price = Q if W < R else Q + (W-R) * S

    result = A_price if A_price < B_price else B_price

    print(f'#{i+1} {result}')