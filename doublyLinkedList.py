#Creating node
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

#values
node1 = Node(5)
node2 = Node(9)
node3 = Node(3)
node4 = Node(8)

#Linking node1
node1.next = node2

#Linking node2
node2.prev = node1
node2.next = node3

#Linking node3
node3.prev = node2
node3.next = node4

#Linking node4
node4.prev = node3

#Traversing Forward
print("\nTraversing forward:")
currentNode=node1
while currentNode:
    print(currentNode.data,end = " -> ")
    currentNode = currentNode.next
print('null')

#Traversing Backwards
print("\nTraversing Backwards:")
currentNode = node4
while currentNode:
    print(currentNode.data, end = " -> ")
    currentNode = currentNode.prev
print('null')
