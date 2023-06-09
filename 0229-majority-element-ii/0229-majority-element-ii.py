class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        # Find potential candidates
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0 and num!=candidate2:
                candidate1 = num
                count1 = 1
            elif count2 == 0 and num!=candidate1:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Validate potential candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        n = len(nums)
        result = []
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        return result
