#Rotate List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        _len = 0
        root = head
        while head:
            _len += 1
            head = head.next
        k %= _len
        if k == 0: return root
        fast, slow = root, root
        while k - 1:
            fast = fast.next
            k -= 1
        pre = slow
        while fast.next:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = None
        fast.next = root
        return slow