class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        answer = len(cards)
        dic = {}
        for i,j in enumerate(cards):
            if(j in dic.keys()):
                answer = min(answer , i-dic[j])
                dic[j] = i
            else:
                dic[j]=i
        if(answer== len(cards)): answer  = -2

        return answer+1        
