class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    node_lst = []
    parts = s.split(' -> ')
    for elem in parts:
        try:
            if isinstance(int(elem), int):
                node_lst.append(int(elem))
        except ValueError:
            pass
    # print(node_lst)
    node = None
    for num in reversed(node_lst):
        node = Node(num, node)
    return node


stringik = "0 -> 1 -> 4 -> 9 -> 16 -> None"
print(linked_list_from_string(stringik))
print(isinstance(linked_list_from_string(stringik), Node))
