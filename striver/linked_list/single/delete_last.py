# Problem Statement: Given a Singly LinkedList, Delete the Last Node in the LinkedList.
# Input: List = 10->20->30->40->null
# Output: 10->20->30->null
# Explanation: Deleted the last node of the linked list.

class Node :
    def __init__(self,data):
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
    
    def deleteLastNode(self):
        if self.head is None:
            return 'List is empty'
        else:
            start = self.head
            while start.next.next is not None:
                start = start.next
            start.next = None
    
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
    print('befor deleting last node:',end='\n')
    LinkedList.printList()
    LinkedList.deleteLastNode()
    print('after deleting last node: ',end='\n')
    LinkedList.printList()

