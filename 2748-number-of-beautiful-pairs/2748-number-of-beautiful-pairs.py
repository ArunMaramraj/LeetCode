class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        
        
        count = 0
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                
                num1 = int(str(nums[i])[0]) 
                num2 = int(str(nums[j])[-1])
                
                mini = min(num1,num2)
                
                booli = True
                for k in range(2,mini+1):
                    if num1%k==0 and num2%k==0 :      
                        booli = False
                        break
                if booli:
                    count+=1
                    
        return count            