# Binary search tree

class TreeNode:

    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

# Build a binary tree
# Searching in binary Tree
"""
The algorithm for searching within a binary search tree is as follows:
1. Designate a node to be the “current node.” (At the beginning of the algorithm, the root node is the first “current node.”)
2. Inspect the value at the current node.
3. If we’ve found the value we’re looking for, great!
4. If the value we’re looking for is less than the current node, search for it
in its left subtree.
5. If the value we’re looking for is greater than the current node, search for
it in its right subtree.
6. Repeat Steps 1 through 5 until we find the value we’re searching for, or
until we hit the bottom of the tree, in which case our value must not be
in the tree.
"""
class BinaryTree:

    def __init__(self, data, left=None, right=None) -> None:
        self.root = TreeNode(data)
        self.root.left = left
        self.root.right = right
        
    def search(self, value: int, node: TreeNode) -> TreeNode: #O(logN)
        if node is None or node.data == value:
            return node
        elif value < node.data:
            return self.search(value, node.left)
        else:
            return self.search(value, node.right)
        
    def insert(self, value, node: TreeNode):
        if value < node.data:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.insert(value, node.left)
        
        elif value > node.data:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.insert(value, node.right)

        return node


    """
    • If the node being deleted has no children, simply delete it.
    • If the node being deleted has one child, delete the node 
    and plug the child into the spot where the deleted node was.
    • When deleting a node with two children, replace the deleted node with
    the successor node. The successor node is the child node whose value is
    the least of all values that are greater than the deleted node.
    • If the successor node has a right child, after plugging the successor node
    into the spot of the deleted node, take the former right child of 
    the successor node and turn it into the left child of 
    the former parent of the successor node.
    """
    def delete(self, value, node: TreeNode):
        if node is None:
            return None
        
        elif value < node.data:
            node.left = self.delete(value, node.left)
            return node
        elif value > node.data:
            node.right = self.delete(value, node.right)
            return node
        elif value == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.right = self.lift(node.right, node)
                return node
    
    def lift(self, node, node_to_delete):
        # If the current node of this function has a left child,
        # we recursively call this function to continue down
        # the left subtree to find the successor node.
        if node.left:
            node.left = self.lift(node.left, node_to_delete)
            return node
        # If the current node has no left child, that means the current node
        # of this function is the successor node, and we take its value
        # and make it the new value of the node that we're deleting:
        else:
            node_to_delete.data = node.data
            # We return the successor node's right child to be now used
            # as its parent's left child:
            return node.right
        
    def traverse_inorder(self, node: TreeNode): #O(N)
        if node is None:
            return
        self.traverse(node.left)
        print(node.data)
        self.traverse(node.right)

    def traverse_preorder(self, node: TreeNode): #O(N)
        if node is None:
            return
        print(node.data)
        self.traverse(node.left)
        self.traverse(node.right)

    def traverse_postorder(self, node: TreeNode): #O(N)
        if node is None:
            return
        self.traverse(node.left)
        self.traverse(node.right)
        print(node.data)

"""
Imagine you were to take an empty binary search tree and insert the
following sequence of numbers in this order: [1, 5, 9, 2, 4, 10, 6, 3, 8].
Draw a diagram showing what the binary search tree would look like.
Remember, the numbers are being inserted in the order presented here

""" 

"""
Write an algorithm that finds the greatest 
value within a binary search tree

Greatest value always at bottom right
"""
def find_gratest_value(node: TreeNode) -> TreeNode:
    if node.right:
        return find_gratest_value(node.right)
    else:
        return node
    



