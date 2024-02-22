class Node:
    def __init__(self, coef=0, exp=0, next=None):
        self.coef = coef
        self.exp = exp
        self.next = next


class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coef, exp):
        if not self.head:
            self.head = Node(coef, exp)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(coef, exp)

    def print_polynomial(self):
        current = self.head
        while current:
            if current.next:
                print(f"{current.coef}x^{current.exp} + ", end="")
            else:
                print(f"{current.coef}x^{current.exp}")
            current = current.next


polynoimal = Polynomial()
polynoimal.insert(3, 2)
polynoimal.insert(2, 1)
polynoimal.insert(1, 0)

polynoimal.print_polynomial()