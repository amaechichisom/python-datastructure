class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.nextnode = None

def cyc_check(node):
    check_marker = node
    marker = node

    while marker!= None and marker.nextnode == None:
        check_marker = check_marker.nextnode
        marker = marker.nextnode.nextnode

        if marker == check_marker:
            return True
    
    return False
