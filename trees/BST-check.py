class Tree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if (self.leftChild == None):
            self.leftChild = Tree(newNode)
        
        else:
            t = Tree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = Tree(newNode)
        else:
            t = Tree(newNode)
            t.leftChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

tree_vals = [2,3,1,5,77,34,67]

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRightChild())

def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)

a = Tree(2)
inorder(a)
sort_check(tree_vals)
