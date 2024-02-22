class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None

    def is_empty(self):
        if self.front==None:
            return True
        return False

    def EnQueue(self,data):
        new_node=Node(data)
        if self.rear==None:
            self.front=self.rear=new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def DeQueue(self):

        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None

def main():
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
    q.DeQueue()
    print("Queue Front : " + str(q.front.data if q.front != None else -1))
    print("Queue Rear : " + str(q.rear.data if q.rear != None else -1))
main()