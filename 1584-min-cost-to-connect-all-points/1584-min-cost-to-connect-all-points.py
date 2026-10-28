class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        ans = 0
        visited = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        
        for _ in range(n):
            u = -1
            curr_min = float('inf')
            for i in range(n):
                if not visited[i] and min_dist[i] < curr_min:
                    curr_min = min_dist[i]
                    u = i
            
            visited[u] = True
            ans += curr_min
            
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist
                        
        return ans
        