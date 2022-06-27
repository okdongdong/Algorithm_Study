# 자기복제수
N = int(input())

for _ in range(N):
    num = input()
    num_length = len(num)
    num2 = str(int(num)**2)
    if num == num2[-num_length:]:
        print('YES')
    else:
        print('NO')
