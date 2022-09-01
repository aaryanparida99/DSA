class Node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        if self.head is None:
            return
        itr = self.head
        lst = " "
        while itr:
            lst += str(itr.data) + "-->"
            itr = itr.next_node
        print(lst)
    
    def insertAtStart(self,data):
        #Inserting data at begining of a Linked List -- O(1)
        node = Node(data,self.head)
        self.head = node
    
    def insertAtEnd(self,data):
        if self.head is None:                                                                                      #Linked List is empty
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next_node:
            itr = itr.next_node
        itr.next_node = Node(data,None)

    def countLength(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next_node
        return count
    
    def insertAtIndex(self,data,idx):                                                    #Considering array like indexing i.e starts from 0
        if idx < 0 or idx > self.countLength():
            raise Exception("Invalid Index")
        if idx == 0:
            self.insertAtStart(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:               
                node = Node(data,itr.next_node)
                itr.next_node = node
                break
            itr = itr.next_node
            count += 1

    def reverse(self):
        prev = None
        curr = self.head
        next = None
        while(curr):
            next = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next
        self.head = prev
        

        
#Driver Code
LL = LinkedList()
LL.insertAtStart(24)
LL.insertAtStart(12)
LL.insertAtEnd(48)
LL.insertAtEnd(64)
LL.printLinkedList()
LL.reverse()
LL.printLinkedList()
