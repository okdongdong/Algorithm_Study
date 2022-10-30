import sys

sys.setrecursionlimit(int(1e6))


class Node:
    def __init__(self, num, people, childs) -> None:
        self.num = num
        self.head = -1
        self.people = people
        self.childs = set(childs) - {-1}

    def set_head(self, head):
        self.head = head

    def del_child(self, child):
        self.childs.discard(child)

    def is_root(self):
        return self.head == -1

    def is_leaf(self):
        return len(self.childs) == 0

    def merge_child(self, child):
        self.people += child.people
        self.del_child(child.num)

    def __gt__(self, other):
        return self.people > other.people

    def __add__(self, other):
        return self.people + other.people

    def __repr__(self) -> str:
        return f'"num": {self.num}, "head": {self.head}, "people": {self.people}, "childs": {self.childs}\n'


def solution(k, num, links):
    n = len(num)

    def make_tree():
        tree = []
        for node_num, childs in enumerate(links):
            tree.append(Node(node_num, num[node_num], childs))

        for node in tree:
            for child in node.childs:
                child = tree[child]
                child.head = node.num

        for node in tree:
            if node.is_root():
                root = node
                break

        return tree, root

    def dfs(now_node, cnt):
        nonlocal now_cnt
        childs = now_node.childs

        if len(childs) == 2:
            left, right = childs
            left, right = tree[left], tree[right]

            dfs(left, cnt)
            dfs(right, cnt)

            if left < right:
                left, right = right, left

            if left.people + right.people + now_node.people <= cnt:
                now_node.merge_child(left)
                now_node.merge_child(right)

            elif right.people + now_node.people <= cnt:
                now_node.merge_child(right)
                now_cnt += 1

            else:
                now_cnt += 2

        elif len(childs) == 1:
            child = (childs | set()).pop()
            child = tree[child]

            dfs(child, cnt)

            if child.people + now_node.people <= cnt:
                now_node.merge_child(child)

            else:
                now_cnt += 1

    min_cnt = max(num)
    max_cnt = sum(num)

    while min_cnt <= max_cnt:
        mid_cnt = (min_cnt + max_cnt) // 2
        now_cnt = 0
        tree, root = make_tree()
        dfs(root, mid_cnt)

        if now_cnt >= k:
            min_cnt = mid_cnt + 1

        else:
            max_cnt = mid_cnt - 1

    return min_cnt


# class Node:
#     def __init__(self, num, people, childs) -> None:
#         self.num = num
#         self.head = -1
#         self.people = people
#         self.childs = set(childs) - {-1}

#     def set_head(self, head):
#         self.head = head

#     def del_child(self, child):
#         self.childs.discard(child)

#     def add_child(self, child):
#         self.childs.add(child)

#     def is_root(self):
#         return self.head == -1

#     def is_leaf(self):
#         return len(self.childs) == 0

#     def merge_child(self, child, grands=[]):
#         self.people += child.people
#         self.del_child(child.num)

#         for grand in grands:
#             self.add_child(grand.num)
#             grand.head = self.num

#     def __gt__(self, other):
#         return self.people > other.people

#     def __repr__(self) -> str:
#         return f'"num": {self.num}, "head": {self.head}, "people": {self.people}, "childs": {self.childs}\n'


# def solution(k, num, links):
#     n = len(num)
#     tree = []
#     for node_num, childs in enumerate(links):
#         tree.append(Node(node_num, num[node_num], childs))

#     que = []
#     for node in tree:
#         for child in node.childs:
#             child = tree[child]
#             child.head = node.num

#     visited = [False] * n
#     for node in tree:
#         head = tree[node.head]

#         if node.is_root() or len(node.childs) + len(head.childs) > 3:
#             continue

#         visited[node.num] = True
#         heappush(que, node)

#     for _ in range(n - k):
#         node = heappop(que)
#         head = tree[node.head]
#         childs = []

#         for child in node.childs:
#             childs.append(tree[child])

#         if node.is_leaf():
#             head.merge_child(node)
#             if visited[head.num]:
#                 heapify(que)
#             else:
#                 visited[head.num] = True
#                 heappush(que, head)

#         elif len(node.childs) + len(head.childs) <= 3:
#             head.merge_child(node, childs)
#             if visited[head.num]:
#                 heapify(que)
#             else:
#                 visited[head.num] = True
#                 heappush(que, head)

#     return max(tree).people


print(
    solution(
        3,
        [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
        [
            [-1, -1],
            [-1, -1],
            [-1, -1],
            [-1, -1],
            [8, 5],
            [2, 10],
            [3, 0],
            [6, 1],
            [11, -1],
            [7, 4],
            [-1, -1],
            [-1, -1],
        ],
    )
)
print(
    solution(
        4,
        [3, 2, 5, 4, 1, 4, 3, 3, 5, 2, 2, 3, 1],
        [
            [1, 2],
            [3, 4],
            [5, -1],
            [6, 7],
            [8, 9],
            [10, -1],
            [-1, -1],
            [-1, -1],
            [-1, -1],
            [-1, -1],
            [11, 12],
            [-1, -1],
            [-1, -1],
        ],
    ),
    10,
)
