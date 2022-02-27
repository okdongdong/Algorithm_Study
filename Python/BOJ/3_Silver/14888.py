# 연산자 끼워넣기
def cal(num, cnt):
    global max_num, min_num

    if cnt == N-1:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        return

    if operators[0]:
        operators[0] -= 1
        cal(num + A_list[cnt+1], cnt+1)
        operators[0] += 1

    if operators[1]:
        operators[1] -= 1
        cal(num - A_list[cnt+1], cnt+1)
        operators[1] += 1

    if operators[2]:
        operators[2] -= 1
        cal(num * A_list[cnt+1], cnt+1)
        operators[2] += 1

    if operators[3]:
        operators[3] -= 1
        if num < 0:
            num *= -1
            num //= A_list[cnt+1]
            num *= -1
        else:
            num //= A_list[cnt+1]
        cal(num, cnt+1)
        operators[3] += 1


N = int(input())
A_list = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_num = -1000000001
min_num = 1000000001

cal(A_list[0], 0)

print(max_num)
print(min_num)
