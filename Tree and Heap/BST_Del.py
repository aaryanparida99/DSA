class BinarySearchTreeNode:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.val = data

## Method definition to do insertion in Binary Search Tree
def insert_BST(root, data):
    if root is None:
      return BinarySearchTreeNode(data)
    else:
      ## It is not allowing duplicate values
      if root.val == data:
        return root
      ## If data is greater than the root element
      ## Traverse at the right hand side
      elif root.val < data:
        root.right = insert_BST(root.right, data)
      else:
      ## If data is lesser than the root element
      ## Traverse at the left hand side
        root.left = insert_BST(root.left, data)
      return root

## Method definition to do inorder traversal
def inorder(root):
  if root:
    inorder(root.left)
    print(root.val, end = " ")
    inorder(root.right)

## Method definition to find minimum value in BST
def minValueNode(node):
  curr = node
  while(curr.left is not None):
    curr = curr.left

  return curr

# Given a binary search tree and a data, this function
# delete the key and returns the new root
def deleteNode(root, data):
    # Base Case
    if root is None:
      return root
    # If the data to be deleted
    # is smaller than the root's
    # data then it lies in left subtree
    if (data < root.val):
      root.left = deleteNode(root.left, data)
 
    # If the data to be delete
    # is greater than the root's
    # data then it lies in right subtree
    elif (data > root.val):
      root.right = deleteNode(root.right, data)
 
    # If data is same as root's data, then this is the node
    # to be deleted
    # Case 1 and Case 2
    else:
        # Node with no child
        # Deleted Node : Leaf Node
        if root.left is None and root.right is None:
          return None
        # Node with only one child
        if root.left is None:
          return root.right
        elif root.right is None:
          return root.left
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        # Case 3
        min_value = minValueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.val = min_value.val
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, min_value.val)
 
    return root

r = BinarySearchTreeNode(50)
r = insert_BST(r, 30)
r = insert_BST(r, 20)
r = insert_BST(r, 40)
r = insert_BST(r, 70)
r = insert_BST(r, 60)
inorder(r)
r = deleteNode(r,20)
print("\nAfter DELETION of 20")
inorder(r)
r = deleteNode(r,60)
print("\nAfter DELETION of 60")
inorder(r)