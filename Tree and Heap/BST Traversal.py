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


def preOrder(root):
    
    if root:       
        print(root.val, " ")
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    
    if root:              
        postOrder(root.left)
        print(root.val, " ")
        postOrder(root.right)


    

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
print("Inorder Traversal")
inorder(r)
print("Preorder Traversal")
preOrder(r)
print("Postorder Traversal")
postOrder(r)
