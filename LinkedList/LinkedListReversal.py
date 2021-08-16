import SinglyLinkedList
 

def link_reversal(node):
    marker = node
    next_marker = None
    prev_marker = None

    while marker:
        next_marker = marker.nextnode

        marker.nextnode = prev_marker

        prev_marker = marker
        marker = next_marker
    
    return prev_marker
        
    

a = SinglyLinkedList.Node(1)
b = SinglyLinkedList.Node(2)
c = SinglyLinkedList.Node(3)

a.nextnode = b
b.nextnode = c

link_reversal(a)
print(b.nextnode.value)
