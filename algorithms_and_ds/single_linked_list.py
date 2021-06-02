# Define Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Define Single linked list class
class SLinkedList:
    def __init__(self):
        self.head = None

    # Size of list
    def size(self):
        nodecount = self.head
        count = 0
        while nodecount is not None:
            count += 1
            nodecount = nodecount.next
        return count

    # Check if list is empty
    def empty(self):
        return False if self.head else True

    # Print list
    def list_print(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    # Add element at front of list
    def push_front(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

    # Add element at end
    def push_back(self, newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            return
        lastval = self.head
        while(lastval.next):
            lastval = lastval.next
        lastval.next = newnode


if __name__ == '__main__':
    ll = SLinkedList()
    ll.head = Node(2)
    val1 = Node(4)
    val2 = Node(5)
    ll.head.next = val1
    val1.next = val2
    ll.push_front(200)
    ll.push_front(80)

    ll.list_print()
    print("Size of list is :", ll.size())
    print("List is empty:", ll.empty())