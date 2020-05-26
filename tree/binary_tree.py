from tree.node import Node


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def search(self, value):
        def traverse(node):
            if node is None: return False
            if node.value is None: return False
            if node.value is not None and node.value == value: return True
            return traverse(node.left) if node.value is not None and value < node.value else traverse(node.right)

        return traverse(self.root)

    def pre_order(self):
        def traverse(node):
            if node is None: return []
            return [node.value] + traverse(node.left) + traverse(node.right)

        return traverse(self.root)

    def post_order(self):
        def traverse(node):
            if node is None: return []
            return traverse(node.left) + traverse(node.right) + [node.value]

        return traverse(self.root)

    def in_order(self):
        def traverse(node):
            if node is None: return []
            return traverse(node.left) + [node.value] + traverse(node.right)

        return traverse(self.root)


def create_tree(data):
    if data is None: return
    value = data[len(data) // 2]
    left_array = data[:len(data) // 2] if len(data) > 1 else None
    right_array = data[(len(data) // 2) + 1:] if len(data) > 1 else None
    return Node(value=value, left=create_tree(left_array), right=create_tree(right_array))


if __name__ == '__main__':
    node = create_tree(sorted([15, 10, 8, 12, 20, 16, 25]))
    binary_tree = BinaryTree(node)
    print(binary_tree.in_order())
    print(binary_tree.pre_order())
    print(binary_tree.post_order())
