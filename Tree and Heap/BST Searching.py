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


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, " ")
        inorder(root.right)
    
def searchBST(root,data):
    if root is None:
        return False
    if data > root.val:
        return searchBST(root.right, data)
    if data < root.val:
        return searchBST(root.left, data)
    else:
        return True
    


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
res = searchBST(r, 22)
print(res)


