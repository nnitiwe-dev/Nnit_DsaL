#Binary
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root=None

    def append(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.insert(self.root,data)

    def insert(self,data_node, data):
        # Compare the new value with the parent node
        if data<data_node.data:
            #go left
            if data_node.left is None:
                data_node.left=Node(data)
            else:
                self.insert(data_node.left,data)
        elif data>data_node.data:
            #go right
            if data_node.right is None:
                data_node.right=Node(data)
            else:
                self.insert(data_node.right,data)

    # Print the tree
    def PrintTree(self,type_="inorder"):
        output=[]
        def _traversal(type_,data_node):
            if type_="inorder":
                _traversal(type_,data_node.left)
                output.append(data_node.data)
                _traversal(type_,data_node.right)

        _traversal(type_,self.root)
        


# Use the insert method to add nodes
BSTree = BST()
BSTree.append(14)
BSTree.append(35)
BSTree.append(31)
BSTree.append(10)
BSTree.append(19)

BSTree.PrintTree("inorder")