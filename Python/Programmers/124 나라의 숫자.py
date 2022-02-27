def solution(n):
    result = []
        
    while n:
        n , temp = divmod(n, 3)
        if not temp:
            n -= 1

        result.append(temp)
    
    result = result[::-1]

    for i in range(len(result)):
        if result[i] == 1:
            result[i] = '1'
        elif result[i] == 2:
            result[i] = '2'
        else: 
            result[i] = '4'
    
    return ''.join(result)


print(1, solution(1))
print(2, solution(2))
print(3, solution(3))
print(6, solution(6))
print(7, solution(7))
print(9, solution(9))
print(10, solution(10))
print(12, solution(12))
print(15, solution(15))