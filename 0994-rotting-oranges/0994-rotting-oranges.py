from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        
        if fresh_count == 0:
            return 0
            
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue and fresh_count > 0:
            minutes += 1
        
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                   
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2  
                        fresh_count -= 1
                        queue.append((row, col))
                        
    
        return minutes if fresh_count == 0 else -1