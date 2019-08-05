class node():
    def __init__(self, value=None):
        self.value = value
        self.child_l = None
        self.child_r = None


def validatorBST(root, min = -2**32, max = 2**32):
    if root == None:
        return True
    if(root.value>min and
       root.value<max and
       validatorBST(root.child_l, min, root.value) and
       validatorBST(root.child_r, root.value, max)):
        return True
    else:
        return False
    
    
root = node(10)
cl = node(5)
cr = node(53)
root.child_l = cl
root.child_r = cr
validatorBST(root)

root1 = node(10)
cl1 = node(53)
cr1 = node(5)
root1.child_l = cl1
root1.child_r = cr1
validatorBST(root1)