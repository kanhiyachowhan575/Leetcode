from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums_str = [str(num) for num in nums]
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
                
        nums_str.sort(key=cmp_to_key(compare))
        
        result = "".join(nums_str)
        return "0" if result[0] == "0" else result
        