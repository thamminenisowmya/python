class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def getHeight(root):
    if root is None:
        # If the node is null, return -1 (height of an empty tree)
        return -1
    else:
# Recursively calculate the height o the left and right subtrees,
        left_height = getHeight(root.right)
        right_height = getHeight(root.right)
# Return the maximum height of the left and right subtrees,
# plus 1 for the current node
        return 1 + max(left_height, right_height)
# Example usage
# constructing a sample binary tree
root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(4)
# Calling getHeight function to get the height of the binary tree
height_of_tree = getHeight(root)
# printing the result
print(" height of the binary tree:", height_of_tree)