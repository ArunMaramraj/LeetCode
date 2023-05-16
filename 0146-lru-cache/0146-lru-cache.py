
class Node:
    
    def __init__(self,key,value):
        self.key,self.value = key,value
        self.prev,self.next=None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.tempcap = 0
        self.hashmap={}
        self.capacity = capacity
        
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev = self.right,self.left
    
    def insert(self,node):
        node.prev = self.right.prev
        self.right.prev.next = node
        node.next = self.right
        self.right.prev=node
        
        
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key: int) -> int:
        
        if(key not in self.hashmap):
            return -1 
        self.remove(self.hashmap[key])
        self.insert(self.hashmap[key])
        return self.hashmap[key].value

    def put(self, key: int, value: int) -> None:   
        if(key in self.hashmap):
            self.remove(self.hashmap[key])
            self.hashmap[key].value = value
            self.insert(self.hashmap[key])
            return None
            
        if self.tempcap == self.capacity:
            lru = self.left.next
            del self.hashmap[lru.key]
            self.remove(lru)
            self.tempcap-=1
            
        temp = Node(key,value)
        self.hashmap[key] = temp
        self.tempcap+=1
        self.insert(temp)
        return None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)