# create a single linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    # intialize head as none
    def __init__(self):
        self.head = None
    
    #insert a value\
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
    def printList(self):
        currentNode = self.head
        while currentNode.next is not None:
            print(currentNode.data,end='->')
            currentNode = currentNode.next
        print(currentNode.data)
if __name__=='__main__':
    firstNode = Node(5)
    linkedlist = LinkedList()
    linkedlist.insert(firstNode)
    secondtNode = Node(7)
    linkedlist.insert(secondtNode)
    thirdNode = Node(9)
    linkedlist.insert(thirdNode)
    linkedlist.printList()    