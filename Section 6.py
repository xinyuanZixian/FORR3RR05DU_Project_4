class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self, d):
        if self.value == d:
            return False
        elif self.value > d:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True

        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True

    def search(self, d):
        if self.value == d:
            return True
        elif self.value > d:
            if self.left:
                return self.left.search(d)
            else:
                return False
        else:
            if self.right:
                return self.right.search(d)
            else:
                return False

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    def search(self, d):
        if self.root:
            return self.root.search(d)
        else:
            return False

t = Tree()
print(t.insert(6))
print(t.insert(2))
print(t.insert(3))
print(t.insert(7))

print(t.search(1))

