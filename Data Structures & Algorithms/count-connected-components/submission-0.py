class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0 
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] *n 

        def dfs(node):
            visited[node] = True 
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)



        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        return components

        