N, L = map(int, input().split())
L_sum = sum(range(1, L))

for i in range(L, 102):

    if i == 101 or N - L_sum < 0:
        result = [-1]
        break

    elif (N-L_sum) % i == 0:
        result = list(range((N-L_sum)//i, (N-L_sum)//i + i))
        break

    L_sum += i

print(*result)

""" 
숫자 리스트에 0이 포함될 수 있다는 점을 놓침
"""
