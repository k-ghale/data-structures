
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop()

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[-1]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


myQueue = Queue()

#Enqueue
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
myQueue.enqueue('D')

print("Queue : ",myQueue.queue)

print("Dequeue : ",myQueue.dequeue())

print("Peek : ",myQueue.peek())

print("isEmpty : ",myQueue.isEmpty())

print("Size : ",myQueue.size())

print("Queue After : ",myQueue.queue)
