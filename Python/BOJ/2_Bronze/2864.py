# 5와 6의 차이

def cal_min_max(N):
    min_N, max_N = '', ''
    for n in N:
        if n == '5' or n == '6':
            min_N += '5'
            max_N += '6'

        else:
            min_N += n
            max_N += n

    return int(min_N), int(max_N)


a, b = input().split()
min_a, max_a = cal_min_max(a)
min_b, max_b = cal_min_max(b)

print(min_a+min_b, max_a+max_b)
