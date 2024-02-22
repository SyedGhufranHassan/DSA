class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add_at_Head(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return

        new_node.next=self.head
        self.head=new_node


    def add_at_index(self, data, index):
            new_node = Node(data)
            current = self.head
            position = 0
            if position == index:
                self.add_at_Head(data)
            else:
                while(current != None and position+1 != index):
                    position = position+1
                    current = current.next

                if current != None:

                    new_node.next = current.next
                    current.next = new_node
                else:
                    print("Index not present")

    def add_at_end(self,data):
            new_node=Node(data)
            if self.head is None:
                self.head=new_node
                return
            current=self.head
            while (current.next):
                current=current.next

            current.next=new_node

    def delete_from_head(self):
        self.head=self.head.next

    def delete_from_tail(self):
        current=self.head
        while (current.next.next):
            current=current.next
        current.next=None

    def delete_from_index(self,index):
        current=self.head
        position=0
        if position==index:
            self.head=self.head.next
            return

        while (current.next.next!=None or position+1 != index):
            position +=1
            current= current.next
        if current!=None:
            current.next=current.next.next
        else:
            print("IN VALID INDEX")

    def delete_from_data(self,data):
        current=self.head
        while (current!=None and current.next.data != data):
            current= current.next
        if current==None:
            print("IN VALID INDEX")
        else:
            current.next=current.next.next
    def length(self):
        current=self.head
        count=0
        while current:
            count +=1
            current=current.next
        return count

    def search_element(self,index):
        current=self.head
        position=0

        while (current.next!=None and position+1 != index):
            position +=1
            current= current.next
        if current.next!=None:
            return current.next.data
        else:
            print("IN VALID INDEX")

    def print(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

    def search_index(self,data):
        current=self.head
        if current.data==data:
            return 0
        index=1
        while (current.next!=None and current.next.data != data):
            index +=1
            current=current.next

        if current.next!=None:
            return index
        else:
            print("WRONG DATA")


def main():

    l=LinkedList()
    l.add_at_Head(3)
    print("ADD AT BEGIN: ")
    l.print()
    l.add_at_index(2,1)
    print("ATT AT INDEX: ")
    l.print()
    l.add_at_end(5)
    print("ADD AT END: ")
    l.print()
    l.delete_from_head()
    print("DELETE FROM HEAD: ")
    l.print()
    l.delete_from_tail()
    print("DELETE FROM TAIL: ")
    l.print()
    l.add_at_Head(9)
    print("ADD AT BEGIN: ")
    l.print()
    l.delete_from_index(1)
    print("DELETE FROM INDEX: ")
    l.print()
    l.add_at_Head(7)
    print("ADD AT BEGIN:")
    l.print()
    l.delete_from_data(9)
    print("DELETE FROM DATA: ")
    l.print()
    l.add_at_Head(6)
    l.add_at_Head(4)
    l.add_at_Head(1)
    print("ADD AT BEGIN: ")
    l.print()

    print("LENGTH OF LINKED LIST: ", l.length())
    print()
    print("AT INDEX", 2 ," ELEMENT IS: ",l.search_element(2))
    print()
    print("DATA", 6 ,"IS AT ",l.search_index(6)," INDEX")
    print()
    print(" END",'\n',"END")
main()