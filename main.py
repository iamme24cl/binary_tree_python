class Binary:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Binary(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Binary(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

def build_binary_tree(root_node, list_of_nodes):
    root = Binary(root_node)
    for node in list_of_nodes:
        root.insert(node)
    return root

nodes = [13, 10, 31, 17, 51, 33]
root = build_binary_tree(56, nodes)
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))
