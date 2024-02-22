class Queue:
    def __init__(self):
        self.queue = []

    def enQueue(self, item):
        self.queue.append(item)

    def deQueue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) < 1:
            return None
        return self.queue[0]

    def isEmpty(self):
        return self.queue == []

    def printQueue(self):
        print(self.queue)

queue = Queue()
print("ENQUEUE")
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
print("QUEUE")
queue.printQueue()
print("DEQUEUE")
print(queue.deQueue())
print("QUEUE")
queue.printQueue()
print("PEEK OF QUEUE")
print(queue.peek())
print("IS EMPTY?? ")
print(queue.isEmpty())