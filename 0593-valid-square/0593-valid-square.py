class Solution:
    import math
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        

        if(p1==p2 or p1==p3 or p1==p4 or p2==p3 or p2==p4 or p3==p4):
            return False
        
        list1 = []
        list1.append(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))
        list1.append(math.sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2))
        list1.append(math.sqrt((p1[0] - p4[0])**2 + (p1[1] - p4[1])**2))
        list1.append(math.sqrt((p2[0] - p4[0])**2 + (p2[1] - p4[1])**2))
        list1.append(math.sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2))
        list1.append(math.sqrt((p3[0] - p4[0])**2 + (p3[1] - p4[1])**2))

        resultant = set(list1)

        if(len(resultant)==2):
            return True
        return False    



        

        
