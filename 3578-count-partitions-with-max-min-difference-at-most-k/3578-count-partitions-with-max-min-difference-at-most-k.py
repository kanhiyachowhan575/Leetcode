class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        
        # dp[i] = number of valid partitions ending at index i
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty prefix has 1 partition
        
        # Prefix sum of dp for O(1) range sum queries
        prefix = [0] * (n + 1)
        prefix[0] = 1
        
        # Two deques to maintain max and min in sliding window
        max_deque = collections.deque()  # decreasing deque for max
        min_deque = collections.deque()  # increasing deque for min
        
        left = 0  # left boundary of current valid window
        
        for i in range(n):
            # Add current element to deques
            while max_deque and nums[max_deque[-1]] <= nums[i]:
                max_deque.pop()
            max_deque.append(i)
            
            while min_deque and nums[min_deque[-1]] >= nums[i]:
                min_deque.pop()
            min_deque.append(i)
            
            # Shrink window from left if invalid
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                # Move left pointer
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1
            
            # Now window [left, i] is valid
            # dp[i+1] = sum(dp[left] to dp[i])
            if left == 0:
                dp[i+1] = prefix[i]  # sum from dp[0] to dp[i]
            else:
                dp[i+1] = (prefix[i] - prefix[left-1]) % MOD
            
            prefix[i+1] = (prefix[i] + dp[i+1]) % MOD
        
        return dp[n] % MOD