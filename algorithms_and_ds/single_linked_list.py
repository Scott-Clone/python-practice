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

    # Returns value at a given index 
    def value_at(self, index):
        findn = self.head
        if findn is None:
            print("List has no itmes")
        count = 0
        while count != index:
            count += 1
            findn = findn.next
        return findn.data

    # Pops and returns front value 
    def pop_front(self):
        if self.head is None:
            return
        front = self.head
        self.head = front.next
        return front.data  
    
    # Pops and returns back value
    def pop_back(self):

        temp = self.head
        if (temp == None):
            return

        if temp is not None:
            while temp.next is not None:
                prev = temp
                temp = temp.next
                poped = temp
            prev.next = None
        return poped.data

    # Return front item
    def front(self):
        return self.head.data
    
    # Return back item
    def back(self):
        x = self.size()
        findval = self.head
        i = 0
        while i < (x - 1):
            findval = findval.next
            i += 1
        return findval.data
    
    # Remove node for a given data
    def remove_node(self, given_data):
        
        temp = self.head
        
        if temp is not None:
            if temp.data == given_data:
                self.head = temp.next
                temp = None
                return
            
        while(temp is not None):
            if temp.data == given_data:
                break
            prev = temp
            temp = temp.next
             
        if(temp == None):
            return
        prev.next = temp.next
        temp = None 

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
    print(ll.value_at(3))

    print(ll.pop_front())
    ll.list_print()
    print(ll.front())
    print(ll.back())
    print(ll.pop_back())

