class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        offset = 10001
        size = 20002
        tree = [0] * size
        
        def update(i, delta):
            while i < size:
                tree[i] += delta
                i += i & (-i)
                
        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s
            
        res = []
        for num in reversed(nums):
            res.append(query(num + offset - 1))
            update(num + offset, 1)
            
        return res[::-1]
        