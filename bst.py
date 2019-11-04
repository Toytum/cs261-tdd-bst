# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.
# Ethan Weikel

class BinarySearchTree:
    

    def __init__(self, val = None):
        self.left = None
        self.key = val
        self.right = None

    def insert(self, child):
        if child.key <= self.key:
            if self.left == None:
                self.left = child
            else:
                self.left.insert(child)
        elif child.key > self.key:
            if self.right == None:
                self.right = child
            else:
                self.right.insert(child)

    def search(self, target):
        if target == self.key:
            return self

        elif target < self.key:
            if self.left != None:
                return self.left.search(target)
            else:
                return None

        elif target > self.key:
            if self.right != None:
                return self.right.search(target)
            else:
                return None

        else:
            return None
        
    def delete(self, target):
        if self.search(target) == None:
            return self
        else:
            if self.search(target) == target:
                if self.right != None:
                    self.right = self

    pass
