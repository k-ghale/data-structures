
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def poppedNode(self):
        if self.isEmpty():
            return "Stack is Empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def StackSize(self):
        return self.size

myStack = Stack()


myStack.push('A')
myStack.push('B')
myStack.push('C')
myStack.push('D')

print("Pop :", myStack.poppedNode())
print("Peek :", myStack.peek())
print("isEmpty :", myStack.isEmpty())
print("Size :", myStack.StackSize())

