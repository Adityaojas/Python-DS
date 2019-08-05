class node():
    def __init__(self, value=None):
        self.value = value
        self.child_l = None
        self.child_r = None
        self.parent = None
        
class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)
        
    def _insert(self, value, node_cur):
        if value < node_cur.value:
            if node_cur.child_l == None:
                node_cur.child_l = node(value)
                node_cur.child_l.parent = node_cur
            else:
                self._insert(value, node_cur.child_l)
            
        elif value > node_cur.value:
            if node_cur.child_r == None:
                node_cur.child_r = node(value)
                node_cur.child_r.parent = node_cur
            else:
                self._insert(value, node_cur.child_r)
        
        else:
            print('value already present in BST')
        
    def show(self):
        if self.root!=None:
            self._show(self.root)

        
    def _show(self, node_cur):
        if node_cur != None:
            self._show(node_cur.child_l)
            print(node_cur.value)
            self._show(node_cur.child_r)
                
            
    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
        
    def _height(self, node_cur, height_cur):
        if node_cur == None:
            return height_cur
        height_l = self._height(node_cur.child_l, height_cur+1)
        height_r = self._height(node_cur.child_r, height_cur+1)
        
        return max(height_l, height_r)
    
    def find(self, value):
        if self.root != None:
            return self._find(self.root, value)
        else:
            return None
        
    def _find(self, node_cur, value):
        if node_cur.value == value:
            return node_cur
        elif value < node_cur.value and node_cur.child_l != None:
            return self._find(node_cur.child_l, value)
        elif value > node_cur.value and node_cur.child_r != None:
            return self._find(node_cur.child_r, value)
        
    def delete(self, value):
        return self.del_node(self.find(value))
    
    def del_node(self, node):
        if node == None or self.find(node.value)==None:
            print('ERROR: value not in tree')
            return None
        
        def node_min_val(node_cur):
            if node_cur != None:
                while node_cur.child_l != None:
                    node_cur = node_cur.child_l
                return node_cur
            else:
                return None
        
        def num_children(node_cur):
            n = 0
            if node_cur.child_l != None:
                n += 1
            if node_cur.child_r != None:
                n += 1
            return n
         
        
        node_parent = node.parent
        n_children = num_children(node)
        
        if n_children == 0:
            if node_parent != None:
                if node == node_parent.child_l:
                    node_parent.child_l = None
                else:
                    node_parent.child_r = None
            else:
                self.root = None
            
        elif n_children == 1:
            if node.child_l != None:
                child = node.child_l
            else:
                child = node.child_r
                
            if node_parent != None:
                if node == node_parent.child_l:
                    node_parent.child_l = child
                else:
                    node_parent.child_r = child
            
            else:
                self.root = child
                
        else:
            node_new = node_min_val(node.child_r)
            node.value = node_new.value
            self.del_node(node_new)
            


"""        
     
import random
def fill_values(bst, n):
    for _ in range(200):
        bst.insert(random.randint(0,n))
    
bst = BinarySearchTree()
fill_values(bst, 500)



bst.show()
bst.height()
bst.find(493)
bst.delete(496)

"""






























        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        