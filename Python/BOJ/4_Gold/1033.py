# 칵테일
import sys

input = sys.stdin.readline


def cal_gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1

    while num2:
        temp = num1 % num2
        num1, num2 = num2, temp

    return num1


def check_materials(material, num, related_material):
    for m in related_materials[material]:
        if m == related_material:
            continue

        materials[m] *= num
        check_materials(m, num, material)


N = int(input())
materials = [1]*N
related_materials = [[] for _ in range(N)]

for _ in range(N-1):
    a, b, p, q = map(int, input().split())

    p *= materials[b]
    q *= materials[a]

    gcd = cal_gcd(p, q)
    p, q = p//gcd, q//gcd

    materials[a] *= p
    check_materials(a, p, a)

    materials[b] *= q
    check_materials(b, q, b)

    related_materials[a].append(b)
    related_materials[b].append(a)

print(*materials)
