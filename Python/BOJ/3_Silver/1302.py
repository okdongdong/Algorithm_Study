# 베스트셀러

N = int(input())
books = [input() for _ in range(N)]
cnt_dic = {}
for book in books:
    try:
        cnt_dic[book] += 1
    except:
        cnt_dic[book] = 1

result = []

for idx, val in cnt_dic.items():
    if val == max(cnt_dic.values()):
        result.append(idx)

print(sorted(result)[0])
