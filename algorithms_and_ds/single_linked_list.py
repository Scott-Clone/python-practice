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
    
    # insert value at index, so current item at that index is pointed to by new item at index

    def insert(self, index, value):

        count = 0
        temp = self.head
        newnode = Node(value)
        
        # if index is zero use previous push front function
        if index == 0:
            self.push_front(value)

        if index != 0:
            # if index out of range return list as is
            if index > self.size():
               return  
            else:
                while count != index:
                    prev = temp
                    temp = temp.next
                    count += 1
                prev.next = newnode
                newnode.next = temp
    
    def erase(self, index):
        
        count = 0
        curr_n = self.head
        
        if curr_n is None:
            return
        
        if index == 0:
            self.pop_front()
        
        elif index >= self.size():
            return
        else:
            while count != index:
                prev_n = curr_n
                curr_n = prev_n.next
                next_n = curr_n.next
                count += 1

            prev_n.next = next_n

    # returns the value of the node at nth position from the end of the list
    def value_n_from_end(self, n):

        temp = self.head
        # use size to get how far n is from the front
        m =  self.size() - n 

        for i in range(0, m - 1):
                temp = temp.next
                i -= 1
        return temp.data
      
            
        

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
    #print(ll.value_at(3))

    #print(ll.pop_front())
    ll.list_print()
    #print(ll.front())
    #print(ll.back())
    #print(ll.pop_back())
    ll.insert(10, 3000)
    ll.list_print()
    ll.erase(2)
    print("pretty")
    ll.list_print()
    print("pretty")
    print(ll.value_n_from_end(2))
