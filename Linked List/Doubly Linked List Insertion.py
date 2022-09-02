class Node:
    def __init__(self,data,next_node = None,prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

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

    def countLength(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next_node
        return count

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        node.prev_node = None
        if self.head is not None:
            self.head.prev_node = node
        self.head = node

    def insert_at_end(self,data):
        itr = self.head
        while itr.next_node:
            itr = itr.next_node
        new_node = Node(data,None,itr)
        itr.next_node = new_node

    def insert_at_idx(self,data,idx):
        if idx < 0 or idx > self.countLength():
            raise Exception("Index out of range")
        if idx == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        count = 0
        while(itr.next_node):                                                                                    #Insertion in between two nodes
            if count == idx - 1:
                new_node = Node(data,itr.next_node,itr)
                itr.next_node.prev_node = new_node
                itr.next_node = new_node
                break
            itr = itr.next_node
            count += 1
        if count == idx - 1:                                                                                     #Insertion at end
            self.insert_at_end(data)
            return





#Driver Code
LL = LinkedList()
LL.insert_at_beginning(24)
LL.insert_at_beginning(52)
LL.insert_at_end(23)
LL.insert_at_end(90)
LL.insert_at_end(346)
LL.insert_at_end(568)
LL.printLinkedList()
LL.insert_at_idx(55, 6)
LL.printLinkedList()
