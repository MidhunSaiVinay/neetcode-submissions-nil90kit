class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        # 0 = unvisited, 1 = visiting (in current DFS path), 2 = done
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1: return False  # cycle
            if state[node] == 2: return True   # already cleared
            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei): return False
            state[node] = 2
            return True

        return all(dfs(i) for i in range(numCourses))