# Digit sum

def Digit_sum(num):
    while num > 9:
        nums = [int(i) for i in str(num)]
        num = sum(nums)
    return num


N = int(input())
answers = [0] * N
for i in range(N):
    answers[i] = '#{0} {1}'.format(i+1,Digit_sum(int(input())))

print('\n'.join(answers))
