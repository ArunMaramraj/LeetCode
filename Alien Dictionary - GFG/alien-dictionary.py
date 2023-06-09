#User function Template for python3

class Solution:
    def findOrder(self,alien_dict, N, K):

        ref = 97
        
        # vertices = set()
    
        # for i in alien_dict:
        #     for j in i :
        #         vertices.add(i)
    
        # V = len(vertices)
    
       
    
        def topoSort(V, adj):
            # Code here
            vis = [False]*V
       
            st = []
            
            def dfs(i):
        
                vis[i] = True
                
                if len(adj[i])>0:
                    for j in adj[i]:
                        if vis[j]:
                            continue
                        else:    
                            dfs(j)
                st.append(i)
        
        
        
            for i in range (V):
                if not vis[i]:
                    dfs(i)
        
            st.reverse()
            return st
    
        adj = [[] for _ in range(K)] 
        for i in range(N-1):
            s1 = alien_dict[i]
            s2 = alien_dict[i+1]
    
            mini = min(len(s1),len(s2))
    
            for i in range(mini):
                if(s1[i]!=s2[i]):
                    adj[ord(s1[i])-ref].append(ord(s2[i])-ref)
                    break
    
    
        topo = topoSort(K,adj)
        ans = ""
        for i in topo:
            ans+=(chr(i+ref))
    
        return ans




                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends