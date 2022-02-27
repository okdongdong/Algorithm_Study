def notation12(number):
    notation = '0123456789ab'
    q, r = divmod(number, 12)
    n = notation[r]
    if number < 12:
        return n   
    return notation12(q) + n


result_lst = []


for num in range(1000, 10000):
    num12 = notation12(num)
    num16 = f'{num:x}'
    sum10, sum12, sum16 = 0, 0, 0

    for n in str(num):
        sum10 += int(n)

    for n in num12:
        sum12 += int(n, 12)
   
    if sum10 != sum12:
        continue        # continue : 조건문 참일시 뒷구문 실행하지 많고 넘김
    else :
        for n in num16:
            sum16 += int(n, 16)

    if sum10 == sum16:
        result_lst.append(num)

print(*result_lst, sep='\n')
            