
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        return self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

#Create a Stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack : ",myStack.stack)
print("Pop : ",myStack.pop())
print("Peek : ",myStack.peek())
print("isEmpty : ", myStack.isEmpty())
print("Size : ", myStack.size())


print("Stack After : ",myStack.stack)
