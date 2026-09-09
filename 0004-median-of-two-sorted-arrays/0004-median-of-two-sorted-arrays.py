class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array for binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # This gives the left partition size
        
        left, right = 0, m
        
        while left <= right:
            partitionX = (left + right) // 2
            partitionY = half - partitionX
            
            # Handle edge cases for out of bounds
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # We have found the correct partition
                if total % 2 == 1:
                    # Odd total length
                    return float(max(maxLeftX, maxLeftY))
                else:
                    # Even total length
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            elif maxLeftX > minRightY:
                # We are too far right in nums1, move left
                right = partitionX - 1
            else:
                # We are too far left in nums1, move right
                left = partitionX + 1
        
        # If we reach here, there is an error (input arrays not sorted or other issue)
        raise ValueError("Input arrays are not sorted or other error.")