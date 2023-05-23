from heapq import heapify,heappush,heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        
        counter = Counter(tasks)
        
        maxheap = [-cnt for cnt in counter.values()]
        
        heapify(maxheap)
        
        q = []
        
        time = 0
        
        while q or maxheap:
            
            time+=1
            
            if maxheap:
                value  = heappop(maxheap)+1
                if(value):
                    q.append([value,time+n])
            
            if q and q[0][1]==time:
                heappush(maxheap,q.pop(0)[0])
                
        return time