class Solution:
    def countTriples(self, n):
        count = 0
        squares = {}
        for i in range(1, n+1):
            squares[i*i] = i
        
        for a in range(1, n+1):
            for b in range(1, n+1):
                c_squared = a*a + b*b
                if c_squared in squares:
                    c = squares[c_squared]
                    if c <= n:
                        count += 1
        
        return count