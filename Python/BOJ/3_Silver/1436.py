N = int(input())

num_lst = ['666']

while True:
    new_lst = []
    for num in num_lst:
        for i in range(10):
            new_lst.append(str(i)+num)  # 숫자 앞에 하나씩 붙일 때
            new_lst.append(num+str(i))  # 숫자 뒤에 하나씩 붙일 때

    num_lst += new_lst
    result = [int(i) for i in num_lst]
    result = list(set(result))  # 중복 값 제거
    if len(result) >= N:
        break

result.sort()
print(result[N-1])

