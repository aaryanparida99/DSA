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

def find_max(root):
    if root is None:
        return -1
    elif root.right is None:
        print(root.val)
    else:
        find_max(root.right)

def find_min(root):
  while(root.left != None):
    root = root.left
  print(root.val)


## Driver Code
r = BinarySearchTreeNode(50)
r = insert_BST(r, 30)
r = insert_BST(r, 20)
r = insert_BST(r, 40)
r = insert_BST(r, 70)
r = insert_BST(r, 60)
r = insert_BST(r, 80)
find_max(r)
find_min(r)