import SinglyLinkedList

# def nth_last(node):
#     prev_marker = None
#     marker = node
#     while marker and marker.nextnode != None:
#         prev_marker = marker
#         marker = marker.nextnode
#     return prev_marker


def nth_to_last_node(n, head):

    left_pointer = head
    right_pointer = head
    for i in range(n-1):
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list')
        
        right_pointer = right_pointer.nextnode
    
    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer


a = SinglyLinkedList.Node(1)
b = SinglyLinkedList.Node(2)
c = SinglyLinkedList.Node(3)
d = SinglyLinkedList.Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(nth_last(a).value)