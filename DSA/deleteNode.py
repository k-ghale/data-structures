
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode  = head
    while currentNode:
        print(currentNode.data, end = ' --> ')
        currentNode = currentNode.next
    print('null')

def deleteSpecificNode(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next
    
    currentNode = head
    while currentNode and currentNode != nodeToDelete:
        currentNode = currentNode.next
    
    if currentNode is None:
        return head

    currentNode.next = currentNode.next.next
    return head


n1 = Node(3)
n2 = Node(2)
n3 = Node(1)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


print("Before deletion: ")
traverseAndPrint(n1)

n1 = deleteSpecificNode(n1,n4)

print("\nAfter deletion")
traverseAndPrint(n1)


