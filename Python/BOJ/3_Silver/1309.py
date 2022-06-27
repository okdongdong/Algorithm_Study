# 동물원
N = int(input())
a = b = c = 1
for _ in range(N):
    temp_a = a
    temp_b = b
    temp_c = c

    a = (temp_a + temp_b + temp_c) % 9901
    b = (temp_a + temp_c) % 9901
    c = (temp_a + temp_b) % 9901

print(a)
