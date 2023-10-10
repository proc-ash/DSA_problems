class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleList:

    # intialize head
    def __init__(self):
        self.head = None
    
    # insert data

    def insertAtLast(self,newNode):
        if self.head is None:
            self.head = newNode
            newNode.prev = self.head
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = newNode
            newNode.prev = current
    
    def deleteAtLast(self):
        if not self.head:
            return 'list is empty'
        else:
            current = self.head

            while current.next.next is not None:
                current = current.next
            current.next.prev = None
            current.next = None
            
    def printList(self):
        if not self.head:
            return 'list is empty'
        else:
            current = self.head

            while current.next.next is not None:
                print(current.data, end= ' <-> ')
                current = current.next
            print(current.data,end=' -> None')

if __name__=='__main__':
    firstNode  =Node(5)
    LinkedList = DoubleList()
    LinkedList.insertAtLast(firstNode)
    secondNode  = Node(7)
    LinkedList.insertAtLast(secondNode)
    thirdNode  = Node(9)
    LinkedList.insertAtLast(thirdNode)
    fourthNode  = Node(11)
    LinkedList.insertAtLast(fourthNode)
    fifthNode = Node(3)
    LinkedList.insertAtLast(fifthNode)
    LinkedList.printList()
    





# # Recursive solution:
# def reverseDLL(head):

#     if not head or not head.next:
#         return head

#     new_head = reverseDLL(head.next)

#     head_next_next = head.next.next
#     head.next.next = head
#     head.next.prev = head_next_next
#     head.prev = head.next
#     head.next = None
#     return new_head

# Iterative solution:
# def reverseDLL(head):
#     prev_temp = None
#     curr = head
#     while curr:
#         curr_next = curr.next  # Store the next node of curr in the original list to ensure that it's not lost during the reversal process.
#         curr.next = prev_temp  # Update the 'next' pointer of the current node to point backwards
#         curr.prev = curr_next  # Update the 'prev' pointer of the current node to point forwards
#         prev_temp = curr       # Move the previous pointer to the current node
#         curr = curr_next       # Move the current pointer to the next node in the original list
#     return prev_temp # At the end return the last node which is now new head 