# 베르트랑 공준

prime_list = [1] * (123456*2+1)
prime_list[0] = 0
prime_list[1] = 0
for i in range(2, int(len(prime_list)**0.5)):
    for j in range(2*i,len(prime_list),i):
        prime_list[j] = 0
    
result = []
while True:
    n = int(input())
    if n == 0:
        break
    result.append(sum(prime_list[2*n:n:-1]))

print(*result, sep='\n')