txt = input()
result = 0
dic={}

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = '22233344455566677778889999'

for i,j in zip(a,b):
    dic[i] = int(j)

for t in txt:
    result += dic[t]+1
print(dic)
print(result)

