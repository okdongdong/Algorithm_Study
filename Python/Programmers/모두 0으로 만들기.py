def solution(a, edges):
    if sum(a):
        return -1

    nodes_list = [set() for _ in range(len(a))]

    for s, e in edges:
        nodes_list[s].add(e)
        nodes_list[e].add(s)

    stack = []
    for now_node, nodes in enumerate(nodes_list):
        if len(nodes) == 1:
            stack.append((now_node, nodes.pop()))

    result = 0

    while stack:
        now_node, next_node = stack.pop()
        temp = a[now_node]

        result += abs(temp)

        a[now_node] = 0
        a[next_node] += temp

        nodes = nodes_list[next_node]
        nodes.discard(now_node)

        if len(nodes) == 1:
            stack.append((next_node, nodes.pop()))

    for num in a:
        if num:
            return -1

    return result
