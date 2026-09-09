#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int totalTime = 0;
        int targetTickets = tickets[k];
        
        for (int i = 0; i < tickets.size(); ++i) {
            if (i <= k) {
                // People in front of or at position k
                totalTime += min(tickets[i], targetTickets);
            } else {
                // People behind position k
                totalTime += min(tickets[i], targetTickets - 1);
            }
        }
        
        return totalTime;
    }
};
