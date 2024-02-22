class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_recursive(value, self.root)

    def _add_recursive(self, value, node):
        if value < node.value:
            if node.left:
                self._add_recursive(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add_recursive(value, node.right)
            else:
                node.right = Node(value)

    def delete(self, value):
        self.root = self._delete_recursive(value, self.root)

    def _delete_recursive(self, value, node):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(value, node.left)
        elif value > node.value:
            node.right = self._delete_recursive(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp_value = self.find_min(node.right)
            node.value = temp_value
            node.right = self._delete_recursive(temp_value, node.right)

        return node

    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def post_order_traversal(self):
        if self.root:
            self._post_order_traversal_recursive(self.root)

    def _post_order_traversal_recursive(self, node):
        if node:
            self._post_order_traversal_recursive(node.left)
            self._post_order_traversal_recursive(node.right)
            print(node.value)

    def in_order_traversal(self):
        if self.root:
            self._in_order_traversal_recursive(self.root)

    def _in_order_traversal_recursive(self, node):
        if node:
            self._in_order_traversal_recursive(node.left)
            print(node.value)
            self._in_order_traversal_recursive(node.right)

    def level_order_traversal(self):
        queue = []
        queue.append(self.root)

        while queue:
            current = queue.pop(0)
            print(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

if __name__ == "__main__":
    bst = BST()

    bst.add(50)
    bst.add(30)
    bst.add(20)
    bst.add(40)
    bst.add(70)
    bst.add(60)
    bst.add(80)

    print("Post order traversal:")
    bst.post_order_traversal()

    print("\nIn order traversal:")
    bst.in_order_traversal()

    print("\nLevel order traversal:")
    bst.level_order_traversal()

    print("\nMin value in BST: ", bst.find_min())
    print("Max value in BST: ", bst.find_max())

    print("\nDeleting value 20...")
    bst.delete(20)

    print("\nIn order traversal after deletion:")
    bst.in_order_traversal()
