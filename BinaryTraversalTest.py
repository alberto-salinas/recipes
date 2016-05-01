import unittest
from datastruct import BiNode
from binarytraversal import *

class BinaryTraversalTest(unittest.TestCase):

    def generateTestTree(self):
        #create left node
        nodeDCE = BiNode("D", BiNode("C"), BiNode("E"))
        left = BiNode("B", BiNode("A"), nodeDCE)

        #create right node
        right = BiNode("G", None, BiNode("I", BiNode("H"), None))

        #put binary tree together
        root = BiNode("F", left, right)
        return root

    def testPreOrder(self):
        preOrder(self.generateTestTree())

    def testInOrder(self):
        inOrder(self.generateTestTree())

    def testPostOrder(self):
        postOrder(self.generateTestTree())

if __name__ == '__main__':
    unittest.main()
