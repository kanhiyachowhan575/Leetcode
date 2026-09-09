class Solution:
    def countOdds(self, low, high):
        # Calculate total numbers in range
        total_numbers = high - low + 1
        
        # If total numbers is even, exactly half are odd
        if total_numbers % 2 == 0:
            return total_numbers // 2
        
        # If total numbers is odd, check if low is odd
        # If low is odd, we have one more odd than even
        return total_numbers // 2 + (1 if low % 2 == 1 else 0)