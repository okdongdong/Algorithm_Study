def isPrime(number):
    for i in range(2,int(number**0.5)+1):
        if not number%i:
            return False
    return True


N = int(input())
nums = [2,3,5,7]
for i in range(N-1):
    temp = []
    for num in nums:
        for n in range(num*10,(num+1)*10):
            if isPrime(n):
                temp.append(n)
            
    nums = temp

print(*nums, sep='\n')

