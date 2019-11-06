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
    
    def has_left_child(self):
        return not (self.left is None)

    def has_right_child(self):
        return not (self.right is None)

    def is_leaf(self):
        return not (self.has_left_child() or self.has_right_child())

    def minimum(self):
        if self.left == None:
            return self
        else:
            return self.left.minimum()

    def delete(self, key):
        if key < self.key:
            if self.has_left_child():
                self.left = self.left.delete(key)
            return self
        elif key > self.key:
            if self.has_right_child():
                self.right = self.right.delete(key)
            return self        
        elif key == self.key:
            if self.is_leaf():
                return None
            elif self.has_left_child() and not self.has_right_child():
                return self.left
            elif self.has_right_child() and not self.has_left_child():
                return self.right
            else:
                new_root = self.right.minimum()
                new_root.right = self.right.delete(new_root.key)
                new_root.left = self.left
                return new_root

    def keys(self, order):
        results = []
        if order == 'pre':
            results.append(self.key)
            if self.left != None:
                self.left.keys(order)
            elif self.right != None:
                self.right.keys(order)
            return results
        # elif order == 'in':
        #     if self.left != None:
        #         self.left.keys(order)
        #     elif self.right != None:
        #         self.right.keys(order)
        #     return results
    pass
