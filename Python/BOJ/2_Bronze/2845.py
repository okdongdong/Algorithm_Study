L, P = map(int, input().split())
people = L * P

newspaper = [int(i) - people for i in input().split()]

print(*newspaper)

