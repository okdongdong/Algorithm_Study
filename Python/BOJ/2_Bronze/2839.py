def Sugar_Delivery(n):  # 5키로 자루를 최대한 확보해야함
    
    cnt3 = 0
    
    while n%5 != 0:     # 총 무게에서 3키로 자루를 하나씩 만들며,
        cnt3 += 1       # 5로 나누어 떨어질 경우 while문 탈출
        n -= 3
        if n < 0:       # n < 0 일 경우 무게를 정확히 맞출 수 없음
            return -1
        
    cnt5 = n//5
    
    return cnt3 + cnt5  # 5키로 자루와 3키로 자루 개수의 합 반환

N = int(input())

print(Sugar_Delivery(N))