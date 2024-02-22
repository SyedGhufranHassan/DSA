class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def is_empty(self):
        if self.head== None:
            return True
        return False

    def push(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def pop(self):
        if self.head==None:
            print("STACK UNDERFLOW")

        else:
            print(self.head.data)
            self.head=self.head.next



    def print(self):
        current=self.head
        while current:
            print(current.data, end=" , ")
            current=current.next

def main():
    s=Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(10)
    s.print()

    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print("AFTER POP $ NUMBER'S FROM THE TOP")
    s.print()

main()
