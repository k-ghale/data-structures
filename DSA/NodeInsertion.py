
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode :
        print(currentNode.data, end = " -> ")
        currentNode = currentNode.next
    print("null")

def InsertANode(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
    
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
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


newNode = Node(7)

print("Before Insertion :")
traverseAndPrint(n1)

InsertANode(n1, newNode, 3)

print("\nAfter Insertion :")
traverseAndPrint(n1)
