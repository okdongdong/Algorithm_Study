N = int(input())

num_lst = [str(i) for i in range(10)]
result = []

while num_lst:
    num = num_lst.pop()
    result.append(int(num))
    
    if int(num[-1]) > 0: 
        for i in range(int(num[-1])):
            new_num = num + str(i)
            num_lst.append(new_num)

result.sort()

try:
    print(result[N])

except:
    print(-1)