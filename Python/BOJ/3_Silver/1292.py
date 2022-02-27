A, B = map(int, input().split())

num_lst = []
# 숫자 리스트 생성
for num in range(1,46):
    for _ in range(num):
        num_lst.append(num)

print(sum(num_lst[A-1:B]))
