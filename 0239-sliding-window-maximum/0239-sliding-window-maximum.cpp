#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq; // Stores indices
        vector<int> result;
        
        for (int i = 0; i < nums.size(); ++i) {
            // 1. Remove indices that are out of the current window bound
            if (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }
            
            // 2. Remove smaller elements from back as they are useless
            while (!dq.empty() && nums[dq.back()] <= nums[i]) {
                dq.pop_back();
            }
            
            // 3. Add current element's index
            dq.push_back(i);
            
            // 4. Append maximum to result once the first window of size k is formed
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }
        
        return result;
    }
};
