class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
    # LEFT CASE
        # check if our new nodes value is less than the current nodes value
        if value < self.value:
            # does it have a child to the left?
            if self.left:
                # place our new node here
                self.left.insert(value)
            # otherwise
                # repeat process for the left
            else:
                self.left = BinarySearchTree(value)
     # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
        elif value >= self.value:
            # does it have a child to the right?
            if self.right:
                # place our new node here
                self.right.insert(value)  
            # otherwise
                # repeat the process for the right 
            else:
                self.right = BinarySearchTree(value)   

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        # BASE CASE
        if self.value == target:
            return True

        # LEFT CASE
        elif self.value > target:
            if self.left == None:
                return False
            return self.left.contains(target) 
        
        # RIGHT CASE
        else:
            if self.right == None:
                return False
            return self.right.contains(target)
