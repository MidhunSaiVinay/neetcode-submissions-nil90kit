class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        visit=set()
        area=0
        
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            area=1
            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    
                    r,c=row+dr,col+dc
                    if (r in range(rows) and c in range(cols)
                    and grid[r][c]==1 and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        area+=1
            return area
                        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    area=max(area,bfs(r,c))
                    
        return area

               
            
