class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def add_at_head(self,data):
        new_node=Node(data)
        new_node.next=self.head
        new_node.prev=None

        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node

    def add_at_tail(self,data):
        if self.head is None:
            self.add_at_head(data)
        new_node=Node(data)
        current=self.head
        while current:
            current=current.next
            if current.next==None:
                break

        current.next=new_node
        new_node.prev=current

    def add_at_index(self,data,index):
        if index==0:
            self.add_at_head(data)

        new_node=Node(data)
        position=0
        current=self.head
        while current.next and position+1 != index:
            current=current.next

        if current.next!=None:
            new_node.next=current.next
            current.next=new_node
            new_node.prev=current

            if new_node.next is not None:
                new_node.next.prev = new_node

    def delete_from_head(self):
        self.head=self.head.next
        self.head.prev=None

    def delete_from_tail(self):
        current=self.head
        while current.next.next:
            current=current.next
        current.next=None

    def delete_from_index(self,index):
        if index==0:
            self.delete_from_head()
        current=self.head
        position=0
        while current.next and position +1 != index:
            position +=1
            current=current.next
        if current.next!=None:
            current.next=current.next.next

    def search(self,index):
        if index==0:
            self.delete_from_head()
        current=self.head
        position=0
        while current.next and position +1 != index:
            position +=1
            current=current.next
        if current.next!=None:
            return current.next.data



    def print(self):
        if self.head is None:
            print("LIST IS EMPTY")
        current=self.head
        while current:
            print(current.data, end="  ")
            current=current.next
