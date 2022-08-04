# 이진수 연산
n = 10**5
a = int(input(), 2)
b = int(input(), 2)
c = (1 << n) - 1

print(bin(a & b)[2:].zfill(n))
print(bin(a | b)[2:].zfill(n))
print(bin(a ^ b)[2:].zfill(n))
print(bin(a ^ c)[2:].zfill(n))
print(bin(b ^ c)[2:].zfill(n))
