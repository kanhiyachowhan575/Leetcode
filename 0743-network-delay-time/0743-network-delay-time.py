import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        pq = [(0, k)]
        visited = set()
        
        while pq:
            time, node = heapq.heappop(pq)
            if node in visited:
                continue
                
            visited.add(node)
            if len(visited) == n:
                return time
                
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (time + weight, neighbor))
                    
        return -1