class node():
    def __init__(self, data=None):
        self.data = data
        self.next = None   
        
class LinkedList():
    def __init__(self):
        self.head = node()
        
    def append(self, value):
        node_new = node(value)
        node_cur = self.head
        while node_cur.next != None:
            node_cur = node_cur.next
        
        node_cur.next = node_new
        
    def length(self):
        total = 0
        node_cur = self.head
        while node_cur.next != None:
            total += 1
            node_cur = node_cur.next
        
        return total
    
    def show(self):
        show = []
        node_cur = self.head
        while node_cur.next != None:
            node_cur = node_cur.next
            show.append(node_cur.data)
        print(show)
        
    def get(self, index):
        if index >= self.length():
            print('ERROR: \'Get\' index out of range')
            return
        node_cur = self.head.next
        i=0
        while i != index:
            node_cur = node_cur.next
            i += 1
        
        return node_cur.data
            
    def delete(self, index):
        if index >= self.length():
            print('ERROR: \'Delete\' index out of range')
            return
        
        node_cur = self.head.next
        i=0
        while i != index:
            node_last = node_cur
            node_cur = node_cur.next
            i+=1
        
        node_last.next = node_cur.next
        return
        
    def __getitem__(self, index):
        return self.get(index)
    
    def insert(self, index, data):
        if index >= self.length():
            self.append(data)
        else:
            node_last = self.head
            node_cur = node_last.next
            i=0
            while i != index:
                node_last = node_cur
                node_cur = node_cur.next
                i += 1
            
            node_new = node(data)
            node_last.next = node_new
            node_new.next = node_cur
        
        return
            
                
            
    
    
lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.show()
lst.delete(2)
lst.show()
lst.get(2)
lst[0]
lst.insert(1,7)
lst.show()
lst.insert(1,6)
lst.show()
lst.insert(0,7)
lst.show()
lst.insert(2,7)
lst.show()
lst.insert(6,7)
lst.show()
lst.insert(8,8)
lst.show()
        
       


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            