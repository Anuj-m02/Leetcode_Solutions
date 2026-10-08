# class Solution:
#     def reversePairs(self, nums):
#         def merge_sort(start, end):
#             if start >= end:
#                 return 0
            
#             mid = (start + end) // 2
#             count = merge_sort(start, mid) + merge_sort(mid + 1, end)
            
#             # Count reverse pairs
#             j = mid + 1
#             for i in range(start, mid + 1):
#                 while j <= end and nums[i] > 2 * nums[j]:
#                     j += 1
#                 count += j - (mid + 1)
            
#             # Merge step
#             temp = []
#             left, right = start, mid + 1
#             while left <= mid and right <= end:
#                 if nums[left] <= nums[right]:
#                     temp.append(nums[left])
#                     left += 1
#                 else:
#                     temp.append(nums[right])
#                     right += 1
#             while left <= mid:
#                 temp.append(nums[left])
#                 left += 1
#             while right <= end:
#                 temp.append(nums[right])
#                 right += 1
#             nums[start:end+1] = temp
            
#             return count

#         return merge_sort(0, len(nums) - 1)

from sortedcontainers import SortedList

# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         l = SortedList()  # Stores elements seen so far (to the left of current)
#         count = 0

#         for a in nums:
#             i = l.bisect_right(2 * a)
#             count += i
#             l.add(a)

#         return len(nums) * (len(nums) - 1) // 2 - count

# from sortedcontainers import SortedList

# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         l = SortedList()
#         count = 0

#         for a in reversed(nums):
#             # We want nums[i] > 2 * nums[j] => nums[i] > 2*a
#             # So find count of nums[i] in l such that nums[i] < a/2
#             count += l.bisect_left(a / 2)
#             l.add(a)

#         return count

class Solution:
    def reversePairs(self, nums):
        return self.mergeSort(nums, 0, len(nums) - 1)

    def countPairs(self, nums, left, mid, right):
        count = 0
        temp = mid + 1

        for i in range(left, mid + 1):
            while temp <= right and nums[i] > 2 * nums[temp]:
                temp += 1

            count += temp - (mid + 1)

        return count

    def mergeSort(self, nums, left, right):
        if left >= right:
            return 0

        mid = left + (right - left) // 2
        count = 0

        count += self.mergeSort(nums, left, mid)
        count += self.mergeSort(nums, mid + 1, right)
        count += self.countPairs(nums, left, mid, right)

        self.merge(nums, left, mid, right)

        return count

    def merge(self, nums, left, mid, right):
        temp = []

        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= right:
            temp.append(nums[j])
            j += 1

        for x in range(len(temp)):
            nums[left + x] = temp[x]