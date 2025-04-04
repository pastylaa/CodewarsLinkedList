class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    if head is None:
        head = Node(data)
    else:
        newNode = Node(data)
        newNode.next = head
        head = newNode
    return head

def build_one_two_three():
    node = None
    node = push(node, 3)
    node = push(node, 2)
    node = push(node, 1)
    return node

chained = None
chained = push(chained, 3)  # 3 -> None
chained = push(chained, 2)  # 2 -> 3 -> None
chained = push(chained, 1)  # 1 -> 2 -> 3 -> None
print(push(chained, 8))  # 8 -> 1 -> 2 -> 3 -> None