class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        candidates.sort()
    
        temp,output = [] , []
        
        def compute(i):
            tempsum = sum(temp)

            if tempsum == target:
                output.append(temp[:])
                return

            if tempsum > target:
                return

            while i < len(candidates):
                temp.append(candidates[i])
                compute(i + 1)
                temp.pop()
                i += 1

                while i < len(candidates) and candidates[i] == candidates[i - 1]:
                    i += 1
                    
        compute(0)
        return output