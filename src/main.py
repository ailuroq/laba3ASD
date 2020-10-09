# Задание: 6.Определить количество элементов в правом поддереве.
from binarytree import tree, bst, heap, Node


class NodeC:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None
        self.rootT = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.rootT = Node(val)
            self.root = NodeC(val)
        else:
            self._add(val, self.root, self.rootT)

    def _add(self, val, node, nodeT):
        if val < node.v:
            if node.l and nodeT.left is not None:
                self._add(val, node.l, nodeT.left)
            else:
                node.l = NodeC(val)
                nodeT.left = Node(val)
        else:
            if node.r and nodeT.right is not None:
                self._add(val, node.r, nodeT.right)
            else:
                node.r = NodeC(val)
                nodeT.right = Node(val)

    def tree_height(self, node):
        left_depth = self.tree_height(node.l) if node.l else 0
        right_depth = self.tree_height(node.r) if node.r else 0
        return max(left_depth, right_depth) + 1

    def find(self):
        if self.root is not None and self.root.r is not None:
            self.root = self.root.r
            return self._find(self.root)
        else:
            return None

    def _find(self, node):
        if node is None:
            return 0
        return self._find(node.l) + 1 + self._find(node.r)

    def deleteTree(self):
        self.root = None

    def returnTree(self):
        return self.rootT

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)
