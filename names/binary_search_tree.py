class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        if self.value is None:
            return None
        # compare to the new value we want to insert
        if self.value > value:
            # If self.left isn't already taken by a node,
            if self.left is None:
                # set the left child to the new node with the new value
                self.left = BSTNode(value)
            else:
                # make that (left) node call insert
                self.left.insert(value)

        else:
            # If self.right isn't already taken by a node,
            if self.right is None:
                # set the right child to the new node with new value
                self.right = BSTNode(value)
            else:
                # otherwise, make that (right) node call insert
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True

        # compare the target to the current value
        # if current value > target
        if self.value > target:
            # check the left subtree
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value <= target
        elif self.value <= target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        if self.right:
            return self.right.get_max()
        else:
            # if we cannot go right, return the current value
            return self.value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # call function on the current value fn(self.value)
        fn(self.value)
        # if you can go left, call for_each on the left tree
        if self.left:
            self.left.for_each(fn)
        # if you can go right, call for_each on the right tree
        if self.right:
            self.right.for_each(fn)