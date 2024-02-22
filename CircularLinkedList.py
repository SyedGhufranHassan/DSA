class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.last=None

    def add_to_empty(self,data):
        if self.last!=None :
            return self.last

        else:
            new_node=Node(data)
            self.last=new_node
            self.last.next=self.last
            return

    def add_at_head(self, data):
        if self.last is None:
            self.add_to_empty(data)

        new_node=Node(data)
        new_node.next=self.last.next
        self.last.next=new_node

        return

    def add_at_tail(self,data):
        if self.last is None:
            self.add_to_empty(data)

        new_node=Node(data)
        new_node.next=self.last.next
        self.last.next=new_node
        self.last=new_node
        return

    def insert_at_between(self,data,index):
        if index==0:
            self.add_to_empty(data)

        position=0
        new_node=Node(data)
        first=self.last.next
        current=self.last.next
        while current.next!=first and position+1 != index:
            position += 1
            current=current.next

        if current.next == first:
            print("IN  VALID INDEX: ")

        else:
            new_node.next=current.next
            current.next=new_node

    def delete_from_head(self):
        if self.last==None:
            return

        self.last.next=self.last.next.next

    def delete_from_tail(self):
        c=self.last
        while c.next!=self.last:
            c=c.next

        c.next=self.last.next
        self.last=c


    def delete(self,i):
        if self.last==None:
            return
        p=0
        c=self.last.next
        while c.next!=self.last.next and p+1!=i:
            c=c.next
            p+=1

        if c.next!=self.last.next:
            c.next=c.next.next





    def print(self):
        if self.last==None:
            print("LIST IS EMPTY")
            return

        temp=self.last.next
        while temp:
            print(temp.data, end="  ")
            temp=temp.next
            if temp== self.last.next:
                break


def main():
    llist = CircularLinkedList()
    print("ADD TO EMPTY")
    last = llist.add_to_empty(6)
    llist.print()
    print()
    print("ADD AT HEAD:")
    last = llist.add_at_head(4)
    llist.print()
    print()
    print("ADD AT HEAD:")
    last = llist.add_at_head(2)
    llist.print()
    print()
    print("ADD AT TAIL:")
    last = llist.add_at_tail(8)
    llist.print()
    print()
    print("ADD AT TAIL:")
    last = llist.add_at_tail(12)
    llist.print()
    print()
    print("ADD AT BETWEEN:")
    last = llist.insert_at_between(10, 2)
    llist.print()
    print()
    print("DELETE FROM HEAD")
    llist.delete_from_head()
    llist.print()
    print()
    print("DELETE FROM TAIL")
    llist.delete_from_tail()
    llist.print()
    print()
    print("DELETE FROM BETWEEN")
    llist.delete(3)
    llist.print()

main()