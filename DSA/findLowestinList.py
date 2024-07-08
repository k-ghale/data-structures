
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue;

n1 = Node(3)
n2 = Node(2)
n3 = Node(1)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print("Lowest Value : ",findLowestValue(n1))
