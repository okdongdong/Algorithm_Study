# 계란으로 계란치기

import sys
input = sys.stdin.readline


def egg_break(inhand, target):
    global max_egg
    if inhand == target: return

    broken = sum(broken_eggs)
    if max_egg < broken:
        max_egg = broken

    if inhand > N-1: 
        return

    if broken_eggs[target]:
        return
    
    if broken_eggs[inhand]:
        for next_target in range(N):
            egg_break(inhand + 1, next_target)
        return
      
    eggs[inhand][0] -= eggs[target][1]
    eggs[target][0] -= eggs[inhand][1]
    if eggs[inhand][0] <= 0:
        broken_eggs[inhand] = 1

    if eggs[target][0] <= 0:
        broken_eggs[target] = 1

    for next_target in range(N):
        egg_break(inhand + 1, next_target)
    
    if broken_eggs[target]:
        broken_eggs[target] = 0

    if broken_eggs[inhand]:
        broken_eggs[inhand] = 0

    eggs[inhand][0] += eggs[target][1]
    eggs[target][0] += eggs[inhand][1]


N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]  # [내구도, 무게]
max_egg = 0
broken_eggs = [0]*N
for target in range(1, N):
    egg_break(0, target)

print(max_egg)
















# class Egg:
#     cnt = 0
#     break_cnt = 0
#
#     def __init__(self, durability, weight) -> None:
#         self.durability = durability
#         self.weight = weight
#         Egg.cnt +=1
#
#     def __del__(self):
#         Egg.break_cnt += 1
#         self.__str__(flag='1')
#
#     def __str__(self,flag ='0'):
#         return flag
#
#     def attack(self, other):
#         self.durability -= other.weight
#         other.durability -= self.weight
#         if self.durability <= 0:
#             self.__del__()
#         if other.durability <= 0:
#             other.__del__()
#
#
# N = int(input())
# eggs = [0]*N
# for i in range(N):
#     durability, weight = map(int, input().split())
#     eggs[i] = Egg(durability, weight)
#
# eggs[0].attack(eggs[2])
#
# eggs[1] = 0
#
# print(eggs)
# for egg in eggs:
#     if str(egg) == '0':
#         print(egg)
# print(Egg.cnt, Egg.break_cnt)
