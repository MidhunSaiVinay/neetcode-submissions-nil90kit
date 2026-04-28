class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < m and 0 <= nc < n
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        for c in range(n):
            dfs(0, c, pac)
            dfs(m-1, c, atl)
        for r in range(m):
            dfs(r, 0, pac)
            dfs(r, n-1, atl)

        return [[r, c] for r, c in pac & atl]