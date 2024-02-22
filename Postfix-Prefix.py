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

    def peek(self):
        return self.head.data

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
            p=self.head.data
            self.head=self.head.next
            return p



    def print(self):
        current=self.head
        while current:
            print(current.data, end=" , ")
            current=current.next

def infix_to_postfix(infix_expr):
    p = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    postfix = []

    for i in infix_expr:
        if i.isalnum():
            postfix.append(i)
        elif i == '(':
            stack.push(i)
        elif i == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while not stack.is_empty() and p.get(i, 0) <= p.get(stack.peek(), 0):
                postfix.append(stack.pop())
            stack.push(i)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return postfix


def evaluate_postfix(postfix_expr):
    stack = Stack()

    for i in postfix_expr:
        if i.isalnum():
            stack.push(int(i))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if i == '+':
                stack.push(operand1 + operand2)
            elif i == '-':
                stack.push(operand1 - operand2)
            elif i == '*':
                stack.push(operand1 * operand2)
            elif i  == '/':
                stack.push(operand1 / operand2)
            elif i == '^':
                stack.push(operand1 ** operand2)

    return stack.pop()


def main():

    stack = Stack()


    infix_expression = "(2-3+4)*(5+6*7)"
    postfix_expression = infix_to_postfix(infix_expression)
    print("Infix Expression:", infix_expression)
    print("Postfix Expression:", postfix_expression)

    result = evaluate_postfix(postfix_expression)
    print("Result of Postfix Expression:", result)


main()