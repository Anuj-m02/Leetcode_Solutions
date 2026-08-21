// class Solution {
// private:
//     long long func(int x, int id, int lm, bool f){
//         long long ans = 0;

//         for(int i = id, i < n; i++){
//             int a = coins[i];
//             long long nlm = (a * lm) / __gcd(a, lm);

//             ans += x / nlm;

//             if(ans > x) continue;

//             if(f){
//                 ans += func(x, i + 1, nlm, !f);
//             }
//             else{
//                 ans -= func(x, i + 1, nlm, !f);
//             }


//         }

//         return ans;

//     }
// public:
//     long long findKthSmallest(vector<int>& coins, int k) {
//         int n = coins.size();
//         long long lo = 1, hi = 1e18;
//         long long mid;
//         long long ways = 0;


//         while(lo <= hi){
//             mid = lo + (hi - lo) / 2;

//             long long ans = func(mid, 0, 1, true);

//             if(ans >= k){
//                 hi = mid - 1;
//                 ways = ans;
//             }
//             else{
//                 lo = mid + 1;
//             }

//         }

//         return ways;

//     }
// };

#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
private:
    int n;

    long long func(long long x, int id, long long lm, bool f) {
        long long count = 0;

        for (int i = id; i < n; i++) {
            long long a = coins[i];
            long long g = std::gcd(a, lm);
            
            // Prevent overflow during LCM calculation
            if (lm / g > x / a) continue; 
            long long nlm = (lm / g) * a;

            if (f) {
                count += (x / nlm) + func(x, i + 1, nlm, !f);
            } else {
                count -= (x / nlm) - func(x, i + 1, nlm, !f);
            }
        }

        return count;
    }

public:
    long long findKthSmallest(vector<int>& coins, int k) {
        this->n = coins.size();
        this->coins = coins;

        long long lo = 1, hi = 1e18;
        long long ans = hi;

        while (lo <= hi) {
            long long mid = lo + (hi - lo) / 2;

            long long ways = func(mid, 0, 1, true);

            if (ways >= k) {
                ans = mid;        // Store 'mid' as the answer, not 'ways'
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        return ans;
    }

private:
    vector<int> coins;
};