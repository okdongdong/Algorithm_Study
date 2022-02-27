# 괄호 추가하기

def cal(nums, operators, cal_type=1):
    global max_val
    val = nums[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            val += nums[i+1]

        elif operators[i] == '-':
            val -= nums[i+1]

        elif operators[i] == '*':
            val *= nums[i+1]

    if cal_type and val > max_val:
        max_val = val

    return val


def bracket(nums, operators, start=0):

    for i in range(start, len(operators)):
        temp_nums = nums[:]
        temp_operators = operators[:]
        if check[i]:
            continue

        if i > 0:
            check[i-1] += 1
        check[i] += 1

        n1 = temp_nums.pop(i)
        n2 = temp_nums.pop(i)
        op1 = temp_operators.pop(i)
        temp_nums.insert(i, cal([n1, n2], [op1], 0))

        cal(temp_nums, temp_operators)
        bracket(temp_nums, temp_operators, i+1)

        if i > 0:
            check[i-1] -= 1
        check[i] -= 1


N = int(input())
expression = input()
nums = []
operators = []

for i in range(N):
    if i % 2:
        operators.append(expression[i])
    else:
        nums.append(int(expression[i]))

check = [0] * len(operators)
max_val = -2**31

cal(nums, operators)
bracket(nums, operators)

print(max_val)
