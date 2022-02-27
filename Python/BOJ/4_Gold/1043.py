# 거짓말

N, M = map(int, input().split())
know_people = list(map(int, input().split()))
party_people = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

if len(know_people) == 1:
    result = len(party_people)

else:
    know_people = set(know_people[1:])
    pre = 0
    now = len(know_people)
    while pre != now:
        pre = len(know_people)

        result = 0
        for party in party_people:
            for people in know_people:
                if people in party:
                    know_people.update(party)
                    break
            else:
                result += 1

        now = len(know_people)

print(result)


# def find_root(num):
#     if num == node[num]:
#         return num
#     node[num] = find_root(node[num])
#     return node[num]

# def union(num1, num2):
#     node[find_root(num2)] = find_root(num1)


# N, M = map(int, input().split())
# know_people = set(list(map(int, input().split()))[1:])
# party_people = [set(list(map(int, input().split()))[1:]) for _ in range(M)]
# result = 0

# node = list(range(N+1))

# if not know_people:
#     result = len(party_people)

# else:
#     head = know_people.pop()
#     know_people.add(head)
#     for party in party_people:
#         if know_people & party:
#             for people in know_people:
#                 union(head, people)
#             know_people.update(party)
#         else:
#             result +=1

# print(result)
