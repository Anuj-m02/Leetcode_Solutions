#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int numberOfCombinations(string num) {
        int n = num.size();
        if (num[0] == '0') return 0;

        int mod = 1e9 + 7;

        // 1. Precompute LCP for O(1) substring comparison
        vector<vector<int>> lcp(n + 1, vector<int>(n + 1, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (num[i] == num[j]) {
                    lcp[i][j] = 1 + lcp[i + 1][j + 1];
                }
            }
        }

        // Safe substring comparison: checks if num[i ... i+len-1] <= num[j ... j+len-1]
        auto is_less_or_equal = [&](int i, int j, int len) -> bool {
            int common = lcp[i][j];
            if (common >= len) return true;
            return num[i + common] <= num[j + common];
        };

        // DP state table initialized to -1 (unvisited)
        vector<vector<int>> memo(n + 1, vector<int>(n + 1, -1));

        auto dp = [&](auto& self, int i, int len) -> int {
            if (i == n) return 1;
            if (len > n - i || num[i] == '0') return 0;

            if (memo[i][len] != -1) return memo[i][len];

            // Option A: Take length strictly GREATER than 'len'
            long long ans = self(self, i, len + 1);

            // Option B: Take length EXACTLY equal to 'len'
            int nxt_i = i + len;

            if (nxt_i == n) {
                // Remaining string forms 1 valid number
                ans = (ans + 1) % mod;
            } else if (nxt_i + len <= n && is_less_or_equal(i, nxt_i, len)) {
                // Valid next number of equal length
                ans = (ans + self(self, nxt_i, len)) % mod;
            } else if (nxt_i + len + 1 <= n) {
                // Next number must be strictly greater in length
                ans = (ans + self(self, nxt_i, len + 1)) % mod;
            }

            return memo[i][len] = ans;
        };

        return dp(dp, 0, 1);
    }
};