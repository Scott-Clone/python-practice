def countComponents(n, edges):
        count = 0
        graph = [[] for _ in range(n)]
        seen = [False for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(node):
            for adj in graph[node]:
                if not seen[adj]:
                    seen[adj] = True
                    dfs(adj)
                    
        for i in range(n):
            if not seen[i]:
                count += 1
                seen[i] = True
                dfs(i)
                
        return count

countComponents(n = 5, edges = [[0,1],[1,2],[3,4]])
