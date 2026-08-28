# from collections import defaultdict , deque , Counter

# class Solution:
#     def lexPalindromicPermutation(self, s: str, target: str) -> str:
        
#         n = len(s)
#         half_len = n//2

#         counts = Counter(s)

#         odd_char = ""
#         for char , count in counts.items() :
#             if count%2 == 1 :
#                 if odd_char :
#                     return ""
#                 odd_char = char
        
#         half_counts = {c : count//2 for c, count in counts.items()}

#         def make_palindrome(left_str) :
#             if n%2 == 1 :
#                 return left_str + odd_char + left_str[::-1]
            
#             return left_str + left_str[::-1]
        

#         # try prefix matching upto half len
#         can_build_prefix = True
#         temp_counts = half_counts.copy()
#         prefix = []

#         for i in range(half_len) :
#             char = target[i]

#             if temp_counts.get(char , 0) > 0 :
#                 prefix.append(char)
#                 temp_counts[char] -= 1
            
#             else :
#                 can_build_prefix = False
#                 break
        
#         if can_build_prefix :
#             cand = make_palindrome("".join(prefix))
#             if cand > target :
#                 return cand
        
#         # longest common prefix now
#         for i in range(half_len - 1 , -1 , -1) :

#             curr_counts = half_counts.copy()

#             for j in range(i) :
#                 curr_counts[target[j]] -= 1
#                 if curr_counts[target[j]] < 0 :
#                     break
            
#             else :

#                 for char in sorted(curr_counts.keys()) :
#                     if char > target[i] and curr_counts[char] > 0 :
#                         curr_counts[char] -= 1


#                         left = list(target[:i]) + [char]
#                         for c in sorted(curr_counts.keys()) :
#                             left.extend([c] * curr_counts[c])
                        
#                         return make_palindrome("".join(left))
        
#         return ""


from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half_len = n // 2
        counts = Counter(s)

        # 1. Check valid palindrome condition
        odd_char = ""
        for char, count in counts.items():
            if count % 2 == 1:
                if odd_char:
                    return ""
                odd_char = char

        half_counts = {c: count // 2 for c, count in counts.items()}

        def make_palindrome(left_str: str) -> str:
            if n % 2 == 1:
                return left_str + odd_char + left_str[::-1]
            return left_str + left_str[::-1]

        # Case 1: Try exact matching the entire half_len prefix of target
        can_build_prefix = True
        temp_counts = half_counts.copy()
        prefix = []

        for i in range(half_len):
            char = target[i]
            if temp_counts.get(char, 0) > 0:
                prefix.append(char)
                temp_counts[char] -= 1
            else:
                can_build_prefix = False
                break

        if can_build_prefix:
            cand = make_palindrome("".join(prefix))
            if cand > target:
                return cand

        # Case 2: Longest common prefix of length i < half_len
        for i in range(half_len - 1, -1, -1):
            curr_counts = half_counts.copy()
            
            # Check if target[:i] can be formed safely
            valid_prefix = True
            for j in range(i):
                ch = target[j]
                if curr_counts.get(ch, 0) <= 0:
                    valid_prefix = False
                    break
                curr_counts[ch] -= 1

            if not valid_prefix:
                continue

            # Try picking a character strictly greater than target[i] at position i
            for char in sorted(curr_counts.keys()):
                if char > target[i] and curr_counts[char] > 0:
                    curr_counts[char] -= 1
                    
                    # Fill the remaining slots greedily with smallest available characters
                    left = list(target[:i]) + [char]
                    for c in sorted(curr_counts.keys()):
                        left.extend([c] * curr_counts[c])

                    return make_palindrome("".join(left))

        return ""