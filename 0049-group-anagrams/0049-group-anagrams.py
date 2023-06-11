class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        dic = defaultdict(list)
        
        for word in strs:
            l = [0]*26
            
            for char in word:
                l[ord(char)-ord('a')]+=1
                
            dic[tuple(l)].append(word)    
            
        return list(dic.values())    