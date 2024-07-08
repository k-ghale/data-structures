
queue = []

#Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
queue.append('D')
print("Queue : ",queue)

#Dequeue
element = queue.pop(0)
print("Dequeue : ",element)

#Peek
frontElement = queue[0]
print("Peek : ",frontElement)

#isEmpty
isEmpty = not bool(queue)
print("isEmpty : ",isEmpty)

#Size
size = len(queue)
print("Size : ",size)
