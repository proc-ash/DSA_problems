# Problem Statement: For a given Singly LinkedList, insert a node at the beginning of the linked list.

# Input: List = 10->20->30->40->null, Node = 0
# Output: 0->10->20->30->40->null
# Explanation: Inserted the given node at the beginning of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleList:
    def __init__(self):
        self.head = None
    
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
    
    def insertAtBegining(self,newNode):
        newNode.next = self.head
        self.head = newNode
    
    def printList(self):
        current = self.head
        while current.next is not None:
            print(current.data, end='->')
            current = current.next
        print(current.data)

if __name__=='__main__':
    firstNode  =Node(5)
    LinkedList = SingleList()
    LinkedList.insert(firstNode)
    secondNode  = Node(7)
    LinkedList.insert(secondNode)
    thirdNode  = Node(9)
    LinkedList.insert(thirdNode)
    fourthNode  = Node(11)
    LinkedList.insert(fourthNode)
    LinkedList.printList()
    fifthNode = Node(3)
    LinkedList.insertAtBegining(fifthNode)
    LinkedList.printList()


