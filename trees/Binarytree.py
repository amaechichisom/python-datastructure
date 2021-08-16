class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if (self.leftChild == None):
            self.leftChild = BinaryTree(newNode)
        
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
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


def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        inorder(tree.getRightChild())
        print(tree.getRootVal())

def preorder(tree):
    if tree != None:
        print(tree.getRootVal())
        inorder(tree.getLeftChild())
        inorder(tree.getRightChild())
        

r = BinaryTree('a')

r.insertLeft('t')
r.insertRight('f')
# print(r.getRootVal())
# print(r.getRightChild())
# print(r.getLeftChild().getRootVal())

print(inorder(r))
print("\n *********************************************")
print(postorder(r))
print("\n *********************************************")
print(preorder(r))