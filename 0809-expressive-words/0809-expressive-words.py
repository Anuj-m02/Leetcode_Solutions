class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        n = len(s)
        cnt = 0

        for word in words:
            m = len(word)
            i, j = 0, 0
            chk = True

            while i < n and j < m:
                if s[i] != word[j]:
                    chk = False
                    break

                # Count group length in s
                len_s = 0
                char_s = s[i]
                while i < n and s[i] == char_s:  # <-- i < n prevents index error
                    i += 1
                    len_s += 1

                # Count group length in word
                len_w = 0
                char_w = word[j]
                while j < m and word[j] == char_w:
                    j += 1
                    len_w += 1

                # Apply LeetCode stretch rules
                if len_s < len_w or (len_s > len_w and len_s < 3):
                    chk = False
                    break

            # Both strings must be completely matched
            if chk and i == n and j == m:
                cnt += 1

        return cnt