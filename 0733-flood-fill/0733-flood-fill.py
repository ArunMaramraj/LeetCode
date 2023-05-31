class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        m = len(image)
        n = len(image[0])
        
        vis = set()
        
        
        def dfs(i,j,tempcolor):
            
            if (i<0 or j<0 or i>=m or j>=n or (i,j) in vis or image[i][j]!=tempcolor ):
                return
            
            
            vis.add((i,j))
            
            dfs(i+1,j , image[i][j])
            dfs(i,j+1 , image[i][j])
            dfs(i,j-1 , image[i][j])
            dfs(i-1,j , image[i][j])
            
            image[i][j] = color
        
        
        dfs(sr,sc,image[sr][sc])
        
        return image
            