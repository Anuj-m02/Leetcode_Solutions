# class Solution:
#     def sortableIntegers(self, nums: list[int]) -> int:
        
#         n = len(nums)
#         sorted_nums = sorted(nums)
#         ans = 0

#         for k in range(1 , n+1) :
#             if n%k != 0 :
#                 continue
            
#             is_sortable = True
#             for i in range(0 , n , k) :
#                 block = nums[i:i+k]
#                 target_block = sorted_nums[i:i+k]

#                 double_block = block + block

#                 found = False
#                 for j in range(k) :
#                     if double_block[j:j+k] == target_block :
#                         found = True
#                         break
                
#                 if not found :
#                     is_sortable = False
#                     break
            
#             if is_sortable :
#                 ans += k
        
#         return ans

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # Pre-calculate divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        total_sum = 0

        for k in divisors:
            is_sortable = True
            
            for i in range(0, n, k):
                # Check if nums[i : i+k] can be rotated to match sorted_nums[i : i+k]
                block = nums[i:i + k]
                target = sorted_nums[i:i + k]
                
                # Check cyclic shift match using standard pattern search or cyclic drop count
                # Count drops in block (cyclic)
                drops = 0
                drop_idx = -1
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        drops += 1
                        drop_idx = j
                
                if drops > 1:
                    is_sortable = False
                    break
                
                # Reconstruct sorted block by rotating
                if drops == 0:
                    rotated = block
                else:
                    # Rotation starts at drop_idx + 1
                    shift = drop_idx + 1
                    rotated = block[shift:] + block[:shift]
                
                if rotated != target:
                    is_sortable = False
                    break
            
            if is_sortable:
                total_sum += k
                
        return total_sum