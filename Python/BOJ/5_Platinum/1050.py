# 물약
from collections import defaultdict, deque
import sys

input = sys.stdin.readline

INF = float("inf")
MAX_PRICE = 1000000001
N, M = map(int, input().split())

prices = {}
recipe_dict = defaultdict(list)
parents = defaultdict(set)
childs = defaultdict(list)

for _ in range(N):
    a, b = input().rstrip().split()
    prices[a] = int(b)

for _ in range(M):
    a, b = input().rstrip().split("=")
    recipe = defaultdict(int)
    for material in b.split("+"):
        recipe[material[1:]] += int(material[0])
        parents[material[1:]].add(a)
    recipe_dict[a].append(recipe)
    childs[a].append(set(recipe.keys()))


def update_price(material, price, visited=set()):
    if material in visited:
        return

    prices[material] = min(price, prices.get(material, INF))
    parent_set = parents[material]

    for parent in parent_set:
        price = INF
        for recipe in recipe_dict[parent]:
            temp = 0
            for mat, cnt in recipe.items():
                if not prices.get(mat):
                    break

                temp += prices[mat] * cnt
            else:
                price = min(price, temp)
        update_price(parent, price, visited | {material})


que = deque(list(prices.keys()))
visited = set()
while que:
    material = que.popleft()
    parent_set = parents[material]
    for parent in parent_set:
        for i in range(len(childs[parent])):
            childs[parent][i].discard(material)

            if not childs[parent][i] and not (parent, i) in visited:
                visited.add((parent, i))
                que.append(parent)
                price = INF
                for recipe in recipe_dict[parent]:
                    temp = 0
                    for mat, cnt in recipe.items():
                        if not prices.get(mat):
                            break

                        temp += prices[mat] * cnt
                    else:
                        price = min(price, temp)
                if prices.get(parent) and prices.get(parent) > price:
                    update_price(parent, price)

                prices[parent] = min(price, prices.get(parent, INF))

result = prices.get("LOVE") or INF
print(-1 if result == INF else min(result, MAX_PRICE))
