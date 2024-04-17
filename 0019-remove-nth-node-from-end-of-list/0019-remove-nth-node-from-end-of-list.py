# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        
        return ans.next
        
        """
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = dummy

        for _ in range(n):
            right = right.next

        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next

        return dummy.next