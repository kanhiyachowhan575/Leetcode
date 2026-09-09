class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
       
        nums1.sort()
        
       
        sorted_nums2 = sorted([(val, i) for i, val in enumerate(nums2)], reverse=True)
        
        res = [0] * len(nums1)
        left, right = 0, len(nums1) - 1
        
       
        
        for val, idx in sorted_nums2:
            if nums1[right] > val:
                res[idx] = nums1[right]
                right -= 1
            else:
                res[idx] = nums1[left]
                left += 1
                
        return res
        