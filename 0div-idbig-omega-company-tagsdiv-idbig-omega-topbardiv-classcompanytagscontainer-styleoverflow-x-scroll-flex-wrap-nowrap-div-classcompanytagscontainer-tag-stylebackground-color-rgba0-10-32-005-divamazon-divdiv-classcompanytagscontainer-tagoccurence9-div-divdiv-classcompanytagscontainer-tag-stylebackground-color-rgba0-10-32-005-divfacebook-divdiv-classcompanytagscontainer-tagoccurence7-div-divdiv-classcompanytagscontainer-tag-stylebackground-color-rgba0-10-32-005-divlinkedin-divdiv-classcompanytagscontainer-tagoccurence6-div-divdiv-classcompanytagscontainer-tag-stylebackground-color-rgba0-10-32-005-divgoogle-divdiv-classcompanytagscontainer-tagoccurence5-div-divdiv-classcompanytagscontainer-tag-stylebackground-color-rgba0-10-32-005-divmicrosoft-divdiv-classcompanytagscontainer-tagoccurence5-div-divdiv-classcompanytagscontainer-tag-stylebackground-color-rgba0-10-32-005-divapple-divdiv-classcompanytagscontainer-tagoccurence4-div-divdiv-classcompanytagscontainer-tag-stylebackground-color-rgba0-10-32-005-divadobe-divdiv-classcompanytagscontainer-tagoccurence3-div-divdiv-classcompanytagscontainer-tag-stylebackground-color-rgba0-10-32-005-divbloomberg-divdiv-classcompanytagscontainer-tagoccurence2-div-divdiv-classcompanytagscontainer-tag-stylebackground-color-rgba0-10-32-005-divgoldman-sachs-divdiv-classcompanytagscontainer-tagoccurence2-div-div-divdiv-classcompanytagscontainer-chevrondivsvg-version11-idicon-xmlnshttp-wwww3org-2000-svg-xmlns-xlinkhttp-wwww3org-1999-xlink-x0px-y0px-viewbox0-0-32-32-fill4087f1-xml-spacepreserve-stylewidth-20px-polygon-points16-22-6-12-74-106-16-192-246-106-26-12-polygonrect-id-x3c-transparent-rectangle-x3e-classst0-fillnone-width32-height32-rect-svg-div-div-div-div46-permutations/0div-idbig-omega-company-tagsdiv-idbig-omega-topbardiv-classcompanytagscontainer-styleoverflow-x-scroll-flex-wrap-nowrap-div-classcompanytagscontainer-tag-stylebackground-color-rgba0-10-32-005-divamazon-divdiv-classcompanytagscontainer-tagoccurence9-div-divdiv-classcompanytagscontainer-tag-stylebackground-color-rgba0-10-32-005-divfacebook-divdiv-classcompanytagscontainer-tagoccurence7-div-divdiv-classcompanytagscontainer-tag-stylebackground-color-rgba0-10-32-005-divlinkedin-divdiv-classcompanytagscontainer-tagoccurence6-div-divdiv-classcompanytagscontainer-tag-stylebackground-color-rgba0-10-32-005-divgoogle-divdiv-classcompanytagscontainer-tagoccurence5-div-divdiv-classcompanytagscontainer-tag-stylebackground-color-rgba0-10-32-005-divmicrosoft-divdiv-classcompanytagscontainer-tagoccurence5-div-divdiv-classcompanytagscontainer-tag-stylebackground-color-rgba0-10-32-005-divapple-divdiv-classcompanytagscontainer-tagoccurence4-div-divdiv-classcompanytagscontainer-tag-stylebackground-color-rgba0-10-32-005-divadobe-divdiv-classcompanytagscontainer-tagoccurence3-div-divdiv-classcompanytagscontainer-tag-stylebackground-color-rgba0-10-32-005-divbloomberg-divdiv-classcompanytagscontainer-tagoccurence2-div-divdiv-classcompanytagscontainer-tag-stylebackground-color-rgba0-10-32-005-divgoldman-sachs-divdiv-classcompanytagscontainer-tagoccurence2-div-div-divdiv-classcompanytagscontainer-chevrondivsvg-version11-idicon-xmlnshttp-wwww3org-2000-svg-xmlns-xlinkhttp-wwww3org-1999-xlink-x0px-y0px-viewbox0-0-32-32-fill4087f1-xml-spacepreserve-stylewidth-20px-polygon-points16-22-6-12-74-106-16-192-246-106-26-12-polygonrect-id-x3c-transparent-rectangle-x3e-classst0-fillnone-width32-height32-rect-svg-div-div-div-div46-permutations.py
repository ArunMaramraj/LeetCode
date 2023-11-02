from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        
        def compute(i, li):
            nonlocal output
            if i == n - 1:
                output.append(li.copy())
                return

            for j in range(i, n):
                li[i], li[j] = li[j], li[i]  # Swap elements
                compute(i + 1, li)
                li[i], li[j] = li[j], li[i]  # Backtrack to the original position

        compute(0, nums) 
        return output
