def insertNodeAtHead(llist, data):
    # Write your code here
    new = SinglyLinkedListNode(data)
    
    if llist is None:
        llist = new
    else:
        newNode = new
        newNode.next = llist
        llist = newNode
        return llist
