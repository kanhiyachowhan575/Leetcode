#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        
        for (char c : s) {
            if (c == '(') st.push(')');
            else if (c == '{') st.push('}');
            else if (c == '[') st.push(']');
            else {
                // If stack is empty or top doesn't match the current closing bracket
                if (st.empty() || st.top() != c) {
                    return false;
                }
                st.pop();
            }
        }
        
        return st.empty();
    }
};
