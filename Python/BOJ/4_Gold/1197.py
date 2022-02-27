# 최소 스패닝 트리
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x:x[2])
visited_list = [{edges[0][0], edges[0][1]}]
result = edges[0][2]
for edge in edges:
    v1, v2, value = edge
    check_idx = -1
    flag = True
    for idx in range(len(visited_list)):
        # print(visited_list)
        if (v1 in visited_list[idx]) and (v2 in visited_list[idx]):
            flag = False
            break
        elif (v1 in visited_list[idx]) or (v2 in visited_list[idx]):
            visited_list[idx].add(v1)
            visited_list[idx].add(v2)

            if check_idx < 0:
                result += value
                check_idx = idx
                flag = False
            else:
                visited_list[check_idx] = visited_list[check_idx]|visited_list[idx]
                visited_list.pop(idx)
                break
    else:
        if flag:
            visited_list.append({v1, v2})
            result += value
        
# print(visited_list)
print(result)