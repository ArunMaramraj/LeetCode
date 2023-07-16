class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        for i in range(n) :
            nums[i] = [nums[i]-k,nums[i]+k]
        
        ans = 0
        count = 0
        data = []

        # storing the x and y
        # coordinates in data vector
        for i in range(len(nums)):

            # pushing the x coordinate
            data.append([nums[i][0], 'x'])

            # pushing the y coordinate
            data.append([nums[i][1], 'y'])

        # sorting of ranges
        data = sorted(data)

        # Traverse the data vector to
        # count number of overlaps
        for i in range(len(data)):

            # if x occur it means a new range
            # is added so we increase count
            if (data[i][1] == 'x'):
                count += 1

            # if y occur it means a range
            # is ended so we decrease count
            if (data[i][1] == 'y'):
                count -= 1

            # updating the value of ans
            # after every traversal
            ans = max(ans, count)
 
        return ans
            
