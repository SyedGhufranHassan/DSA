class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_node_recursive(value, self.root)

    def _add_node_recursive(self, value, node):
        if value < node.value:
            if node.left:
                self._add_node_recursive(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add_node_recursive(value, node.right)
            else:
                node.right = Node(value)

    def pre_order_traversal(self):
        if self.root:
            print(self.root.value)
            self._pre_order_traversal_recursive(self.root.left)
            self._pre_order_traversal_recursive(self.root.right)

    def _pre_order_traversal_recursive(self, node):
        if node:
            print(node.value)
            self._pre_order_traversal_recursive(node.left)
            self._pre_order_traversal_recursive(node.right)

    def post_order_traversal(self):
        if self.root:
            self._post_order_traversal_recursive(self.root.left)
            self._post_order_traversal_recursive(self.root.right)
            print(self.root.value)

    def _post_order_traversal_recursive(self, node):
        if node:
            self._post_order_traversal_recursive(node.left)
            self._post_order_traversal_recursive(node.right)
            print(node.value)

    def find_node(self, value):
        return self._find_node_recursive(value, self.root)

    def _find_node_recursive(self, value, node):
        if node is None:
            return None
        elif node.value == value:
            return node
        elif value < node.value:
            return self._find_node_recursive(value, node.left)
        else:
            return self._find_node_recursive(value, node.right)


tree = Tree()
tree.add_node(5)
tree.add_node(2)
tree.add_node(8)
tree.add_node(1)
tree.add_node(4)
tree.add_node(7)

print("Pre order traversal:")
tree.pre_order_traversal()

print("Post order traversal:")
tree.post_order_traversal()

node = tree.find_node(7)
if node:
    print(f"Node with value {node.value} found.")
else:
    print("Node not found.")
