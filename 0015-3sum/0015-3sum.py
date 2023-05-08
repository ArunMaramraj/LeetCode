class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort()
        output = []

        for i in range (len(nums)):
            if(nums[i] == nums[i-1] and i>=1):
                continue
            else:
                l= i+1
                r = len(nums)-1
                
                while(l<r):
                    if(nums[i] + nums[l] + nums[r] < 0 ):
                        l+=1
                    elif(nums[i] + nums[l] + nums[r] > 0):
                        r-=1
                    else:
                        output.append([nums[i], nums[l], nums[r]])

                        pointer = l+1

                        while(pointer < r and nums[pointer]==nums[l]):
                            pointer+=1
                        
                        l = pointer      
        
        return output
                                

                    

       


          




                    

                    


