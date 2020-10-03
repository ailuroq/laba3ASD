# Задание: 6.Определить количество элементов в правом поддереве.
class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

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

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)


#     3
# 0     4
#   2      8
tree = Tree()
tree.add(8)
tree.add(12)
tree.add(10)
tree.add(9)
tree.add(11)
tree.add(14)
tree.add(13)
tree.add(15)
tree.add(4)
tree.add(6)
tree.add(17)
tree.printTree()
print("answer")
print(tree.find())
tree.deleteTree()
tree.printTree()
