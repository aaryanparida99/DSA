class BinarySearchTree:
   def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None


def insert_BST(root, data):
    if root is None :
        return BinarySearchTree(data)
    else:
        if root.val == data:
            return root
        elif root.val < data:
            root.right = insert_BST(root.right, data)
        elif root.val > data:
            root.left = insert_BST(root.left, data)
        return root


def minValue(root):
    curr = root
    while(curr.left != None):
        curr = minValue(curr.left)
    return curr
 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end = " ")
        inorder(root.right)

def delNode(root,data):
    if root is None:
        return root
    elif root.val < data:
        root.right = delNode(root.right, data)
    elif root.val > data:
        root.left = delNode(root.left, data)
    
    else:
        if root.left is None and root.right is None:
            return None
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        min = minValue(root.right)
        root.val = min.val
        root.right = delNode(root.right, min.val)
    
    return root



#Driver Code
r = BinarySearchTree(56)
r = insert_BST(r ,21)
r = insert_BST(r , 34)
r = insert_BST(r ,9)
r = insert_BST(r ,23)
r = insert_BST(r ,34)
r = insert_BST(r ,256)
r = insert_BST(r ,89)
r = insert_BST(r ,12)
inorder(r)
delNode(r,21)
print("\nPost Deletion")
inorder(r)

