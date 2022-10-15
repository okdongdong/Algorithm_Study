from asyncio.windows_events import NULL
from heapq import heapify, heappop, heappush


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

    def add_child(self, child):
        self.childs.add(child)

    def is_root(self):
        return self.head == -1

    def is_leaf(self):
        return len(self.childs) == 0

    def merge_child(self, child, grands=[]):
        self.people += child.people
        self.del_child(child.num)

        for grand in grands:
            self.add_child(grand.num)
            grand.head = self.num

    def __gt__(self, other):
        return self.people > other.people

    def __repr__(self) -> str:
        return f'"num": {self.num}, "head": {self.head}, "people": {self.people}, "childs": {self.childs}\n'


def solution(k, num, links):
    n = len(num)
    nodes = []
    for node_num, childs in enumerate(links):
        nodes.append(Node(node_num, num[node_num], childs))

    que = []
    for node in nodes:
        for child in node.childs:
            child = nodes[child]
            child.head = node.num

    visited = [False] * n
    for node in nodes:
        head = nodes[node.head]

        if node.is_root() or len(node.childs) + len(head.childs) > 3:
            continue

        visited[node.num] = True
        heappush(que, node)

    for _ in range(n - k):
        node = heappop(que)
        head = nodes[node.head]
        childs = []

        for child in node.childs:
            childs.append(nodes[child])

        if node.is_leaf():
            head.merge_child(node)
            if visited[head.num]:
                heapify(que)
            else:
                visited[head.num] = True
                heappush(que, head)

        elif len(node.childs) + len(head.childs) <= 3:
            head.merge_child(node, childs)
            if visited[head.num]:
                heapify(que)
            else:
                visited[head.num] = True
                heappush(que, head)

    return max(nodes).people


# print(
#     solution(
#         3,
#         [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
#         [
#             [-1, -1],
#             [-1, -1],
#             [-1, -1],
#             [-1, -1],
#             [8, 5],
#             [2, 10],
#             [3, 0],
#             [6, 1],
#             [11, -1],
#             [7, 4],
#             [-1, -1],
#             [-1, -1],
#         ],
#     )
# )
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
