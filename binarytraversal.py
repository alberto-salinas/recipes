
def preOrder(root):
    if (root is None):
        return
    print root.getData()
    preOrder(root.getLeft())
    preOrder(root.getRight())

def inOrder(root):
    if (root is None):
        return
    inOrder(root.getLeft())
    print root.getData()
    inOrder(root.getRight())

def postOrder(root):
    if(root is None):
        return
    postOrder(root.getLeft())
    postOrder(root.getRight())
    print root.getData()
