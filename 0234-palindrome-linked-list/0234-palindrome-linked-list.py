# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if not head :
            return None
        prev = None
        temp = head
        while temp :
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next :
            return True
        slow = fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        second_half = self.reverse(slow)
        first_half = head
        while second_half :
            if first_half.val != second_half.val :
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         # Helper to clone the list
#         def clone(node):
#             dummy = ListNode(0)
#             curr = dummy
#             while node:
#                 curr.next = ListNode(node.val)
#                 curr = curr.next
#                 node = node.next
#             return dummy.next

#         # Helper to reverse a linked list
#         def reverse(node):
#             prev = None
#             while node:
#                 next_temp = node.next
#                 node.next = prev
#                 prev = node
#                 node = next_temp
#             return prev

#         # Clone and reverse
#         cloned = clone(head)
#         reversed_clone = reverse(cloned)

#         # Compare original and reversed clone
#         while head and reversed_clone:
#             if head.val != reversed_clone.val:
#                 return False
#             head = head.next
#             reversed_clone = reversed_clone.next

#         return True
