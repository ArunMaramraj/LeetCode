class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if((len(points)==1 or len(points) ==2)):
            return len(points)
        else:
            ans = 0
            for i in range (len(points)-1):
                dic = {}
                for j in range(i+1,len(points)):
                    dx = points[j][0] - points[i][0]
                    dy = points[j][1] - points[i][1]

                    if(dx==0):
                        if(inf in dic.keys()):
                            dic[inf]+=1
                        else:
                            dic[inf] = 1
                    else:
                        if(dy/dx in dic.keys()):
                            dic[dy/dx]+=1
                        else:
                            dic[dy/dx] = 1
                ans = max(ans,max(dic.values())+1)            
        return ans

              
                   