# 92. Reverse Linked List II

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(left - 1):
            p = p.next
        cur = p.next
        pre = None
        for _ in range(right - left + 1):
            cur.next, pre, cur = pre, cur, cur.next
        p.next.next = cur
        p.next = pre
        return dummy.next
        
        return dummyNode.next

        # Solution 2
        def reverseBetween(self, head, m, n):
            if m >= n:
                return head
            #Step 1#    
            ohead = dummy = ListNode(0)
            whead = wtail = head
            dummy.next = head
            for i in range(n-m):
                wtail = wtail.next
            #Step 2#  
            for i in range(m-1):
                ohead, whead, wtail = whead, whead.next, wtail.next
            #Step 3#  
            otail, wtail.next = wtail.next, None
            revhead, revtail = self.reverse(whead)
            #Step 4#  
            ohead.next, revtail.next = revhead, otail
            return dummy.next
                
        def reverse(self, head):
            pre, cur, tail = None, head, head
            while cur:
                cur.next, pre, cur = pre, cur, cur.next
            return pre, tail