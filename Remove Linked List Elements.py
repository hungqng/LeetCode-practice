# 203. Remove Linked List Elements

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev, curr = dummy, head
        
        while curr:
            nxt = curr.next
            
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt
        return dummy.next

        # Solution 2
        if not head: return None
        head.next = self.removeElements(head.next, T);
        return head.next if head.val == T else head