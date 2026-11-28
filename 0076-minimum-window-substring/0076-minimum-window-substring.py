from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if n < m:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)

        left = 0
        right = 0
        formed = 0
        window_cnt = defaultdict(int)
        ans = float("inf"), None, None

        while right < n:
            char = s[right]
            window_cnt[char] += 1

            if char in dict_t and window_cnt[char] == dict_t[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                # Save smallest valid window
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                window_cnt[char] -= 1
                if char in dict_t and window_cnt[char] < dict_t[char]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

