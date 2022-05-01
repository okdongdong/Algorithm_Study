# 물약
import sys

input = sys.stdin.readline


def cal_price(now_recipe, material):
    # 무한루프일 경우 -1 반환
    if material in now_recipe:
        if material_price.get(material) and min_price.get(material) and min_price[material] > -1:
            min_price[material] = min(material_price.get(
                material), min_price.get(material))
            return min_price[material]

        if min_price.get(material) and min_price[material] > -1:
            return min_price.get(material)

        if material_price.get(material):
            min_price[material] = material_price[material]
            return material_price[material]

        return -1

    price_list = []
    if material_price.get(material):
        if recipe_dict.get(material):
            price_list.append(material_price[material])

        else:
            if min_price.get(material):
                return min(material_price[material], min_price[material])

            return material_price[material]

    if not recipe_dict.get(material):
        return -1

    if min_price.get(material) and min_price[material] > -1:
        return min_price[material]

    for recipe in recipe_dict[material]:
        price = 0

        for mat, cnt in recipe.items():
            now_price = cal_price(now_recipe | set([material]), mat)

            # 무한루프 체크
            if now_price == -1:
                break

            price += now_price*cnt

        else:
            if price:
                price_list.append(price)

    if price_list:
        if min_price.get(material) and min_price[material] > -1:
            min_price[material] = min(min_price[material], min(price_list))
        else:
            min_price[material] = min(price_list)

        return min_price[material]

    return -1


N, M = map(int, input().split())

material_price = {}
recipe_dict = {}
min_price = {}

for _ in range(N):
    material, price = input().split()
    material_price[material] = int(price)

for _ in range(M):
    menu, material_temp = input().rstrip().split('=')
    if not recipe_dict.get(menu):
        recipe_dict[menu] = []

    materials = material_temp.split('+')
    temp_dict = {}
    for material in materials:
        for i in range(len(material)):
            if not material[i].isdigit():
                cnt = int(material[:i])
                mat = material[i:]

                if temp_dict.get(mat):
                    temp_dict[mat] += cnt
                else:
                    temp_dict[mat] = cnt

                break

    recipe_dict[menu].append(temp_dict)


cal_price(set(), 'LOVE')

if min_price.get('LOVE') and min_price['LOVE'] > -1:
    print(min_price['LOVE'] if min_price['LOVE']
          <= 1000000000 else 1000000001)

elif material_price.get('LOVE'):
    print(material_price['LOVE'])

else:
    print(-1)
