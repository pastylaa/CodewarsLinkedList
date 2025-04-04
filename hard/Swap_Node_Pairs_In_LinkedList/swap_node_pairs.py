class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def swap_pairs(head):
    if not head or not head.next:
        return head

    new_head = head.next
    prev = None
    current = head

    while current and current.next:
        first = current
        second = current.next

        first.next = second.next
        second.next = first

        if prev:
            prev.next = second

        prev = first
        current = first.next

    return new_head
