class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(5)
node2 = Node(3)
node3 = Node(7)
node4 = Node(1)

#Linking node1
node1.next = node2

#Linking node2
node2.next = node3

#Linking node3
node3.next = node4

#Linking node4
node4.next = node1

print("\nTraversing :")
currentNode = node1
startNode = node1

print(currentNode.data,end = " ->")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data,end = " -> ")
    currentNode = currentNode.next

print('...')
