class Node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    #insert at start
    def push(self,data):   
        new_node = Node(data)
        temp = self.head
        new_node.next_node = self.head

        if self.head is not None:
            while(temp.next_node != self.head):
                temp = temp.next_node
            temp.next_node = new_node
        else:
            new_node.next_node = new_node                                                                                   #Linked List is empty

        self.head = new_node

    def printLinkedList(self):
        itr = self.head
        while(True):
            print(itr.data, end= "-->")
            itr = itr.next_node
            if (itr == self.head):
                break


#Driver Code
LL = LinkedList()
LL.push(20)
LL.push(12)
LL.push(30)
LL.printLinkedList()

