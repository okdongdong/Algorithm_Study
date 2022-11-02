from collections import defaultdict

N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]
students_sets = [set() for _ in range(N)]

for grade in range(5):
    class_cnts = defaultdict(set)
    for i in range(N):
        classroom = students[i][grade]
        class_cnts[classroom].add(i)

    for i in range(N):
        classroom = students[i][grade]
        students_sets[i] |= class_cnts[classroom]

students_scores = list(map(len, students_sets))
print(students_scores.index(max(students_scores)) + 1)
