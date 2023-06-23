def solution(n, computers):
    def dfs(v):
        visited[v] = True#방문처리
        
        #인접노드 탐구
        for nei in range(n):
            #방문x + 인접할 때
            if not visited[nei] and computers[v][nei]:
                dfs(nei)
    count = 0
    visited = [False] * (n)#노드별 방문여부
    
    for node_idx in range(n):
        if not visited[node_idx]:
            dfs(node_idx)
            count += 1
            
    return count