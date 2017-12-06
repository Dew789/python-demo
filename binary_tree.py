class BinTNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return self.data

class BinTree(object):

    def __init__(self):
        self._root = None
        self._queue = []

    def root(self):
        return self._root

    def is_empty(self):
        return self._root

    def add(self, data):
        node = BinTNode(data)
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

    def recur_preorder(self):
        root = self._root
        if root is None:
            return
        print(root)
        recur_preorder(root.left)
        recur_preorder(root.right)

    def recur_inorder(self):
        root = self._root
        if root is None:
            return
        recur_preorder(root.left)
        print(root)
        recur_preorder(root.right)

    def recur_postorder(self):
        root = self._root
        if root is None:
            return
        recur_preorder(root.left)
        recur_preorder(root.right)
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

    def posorder(self):
        if self._root is None:
            return
        stack1 = []
        stack2 = []
        node = self._root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(left)
            if node.right:
                stack1.append(right)
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
