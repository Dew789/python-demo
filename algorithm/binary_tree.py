class Node(object):

    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


class BinaryTree(object):

    def __init__(self):
        self._root = None
        self._queue = []

    def root(self):
        return self._root

    def is_empty(self):
        return self._root

    def add(self, data):
        node = Node(data)
        if self._root is None:
            self._root = node
            self._queue.append(node)
        else:
            curr_node = self._queue[0]
            if curr_node.left is None:
                curr_node.left = node
                self._queue.append(node)
            else:
                curr_node.right = node
                self._queue.append(node)
                self._queue.pop(0)
        return node

    def recur_preorder(self, root):
        if root is None:
            return
        print(root)
        self.recur_preorder(root.left)
        self.recur_preorder(root.right)

    def recur_inorder(self, root):
        if root is None:
            return
        self.recur_inorder(root.left)
        print(root)
        self.recur_inorder(root.right)

    def recur_postorder(self, root):
        if root is None:
            return
        self.recur_postorder(root.left)
        self.recur_postorder(root.right)
        print(root)

    def preorder(self):
        if self._root is None:
            return
        stack = []
        node = self._root
        while node or stack:
            while node:
                print(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

    def inorder(self):
        if self._root is None:
            return
        stack = []
        node = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node)
            node = node.right

    def pos_order(self):
        if self._root is None:
            return
        stack1 = []
        stack2 = []
        node = self._root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        for node in stack2[::-1]:
            print(node)

    def level(self):
        if self._root is None:
            return
        queue = []
        queue.append(self._root)
        while queue:
            node = queue.pop(0)
            print(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
                
    def reverse(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            tmp = node.left
            node.left = node.right
            node.right = tmp

    @staticmethod
    def find_lca(root, n1, n2):
        if not root :
            return None
        if (root is n1) or (root is n2):
            return root
        left = BinaryTree.find_lca(root.left, n1, n2)
        right = BinaryTree.find_lca(root.right, n1, n2)
        if left and right:
            return root
        else:
            return left or right

    def lowest_common_ancestor(self, node_1, node_2):
        BinaryTree.find_lca(self._root, node_1, node_2)


if __name__ == '__main__':
    t = BinaryTree()
    for i in range(10):
        if i == 3:
            a = t.add(i)
            continue
        if i == 9:
            b = t.add(i)
            continue
        t.add(i)
    t.lowest_common_ancestor(a, b)
