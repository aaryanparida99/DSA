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
    
    def insertAtIndex(self,data,idx):                                                   
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
    
    #Remove a node based on index passed(Considering index starts at 0)
    def removeNode(self,idx):
        if idx < 0 or idx > self.countLength():
            raise Exception("Invalid Index")
        if idx == 0:                                                                                          #First node is to be removed
            self.head = self.head.next_node
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:               
                itr.next_node = itr.next_node.next_node
                break
            itr = itr.next_node
            count += 1

        
#Driver Code
LL = LinkedList()
LL.insertAtStart(24)
LL.insertAtStart(12)
LL.insertAtEnd(48)
LL.insertAtEnd(64)
LL.printLinkedList()
LL.insertAtIndex(10,1)
LL.printLinkedList()
LL.removeNode(2)
LL.printLinkedList()
