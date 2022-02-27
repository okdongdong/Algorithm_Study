# 에너지 드링크

N = int(input())
drink = [int(i) for i in input().split()]
max_drink = max(drink)
result = (max_drink + sum(drink))*0.5
print(result)