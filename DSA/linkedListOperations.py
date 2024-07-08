
#Traversal
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def TraversalAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end = " -> ")
        currentNode = currentNode.next
    print("null")

n1 = Node(7)
n2 = Node(2)
n3 = Node(3)
n4 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4

TraversalAndPrint(n1)


