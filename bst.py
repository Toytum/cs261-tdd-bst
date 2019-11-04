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
            if self.left != None:
                self.left.insert(child)
            else:
                self.left = child

        elif child.key > self.key:
            if self.right != None:
                self.right.insert(child)
            else:
                self.right = child
    
    def delete(self, val):
        if val == self.key:
            return None
        else:
            return self

    def search(self, val):
        if val == self.key:
            return self

        elif val <= self.key:
            if self.left != None:
                self.left.search(val)
            else:
                return None 

        elif val > self.key:
            if self.right != None:
                self.right.search(val)
            else:
                return None
    pass
