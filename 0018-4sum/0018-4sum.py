class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        output = []
        n = len(nums)
        i = 0
        nums.sort()
        while (i<n-1):
            j = i+1
            while(j<n-1):
                l = j+1
                r = n-1

                temptarget = target - nums[i] - nums[j]
                while(l<r):
                    if(nums[l] + nums[r] > temptarget):
                        r-=1
                    elif(nums[l] + nums[r] < temptarget):
                        l+=1
                    else:
                        output.append([nums[i], nums[j], nums[l], nums[r]])
                        templeft = l+1
         
                        while(templeft<r and nums[l]==nums[templeft] ):
                            templeft+=1
                        l = templeft

                tempj = j+1
                while(tempj<n and nums[tempj] == nums[j] ):
                    tempj+=1
                j = tempj    


            tempi = i+1
            while(tempi<n and nums[tempi]==nums[i]):
                tempi+=1
            i=tempi    

        return output



