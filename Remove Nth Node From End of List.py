# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
            
        #delete
        left.next = left.next.next
        return dummy.next

        #One Pointer
    #   ptr, length = head, 0
	#   while ptr:
	# 	    ptr, length = ptr.next, length + 1
	#   if length == n : return head.next
	#   ptr = head
	#   for i in range(1, length - n):
	# 	    ptr = ptr.next
	#   ptr.next = ptr.next.next
	#   return head

        #Two Pointer
        # fast = slow = head
	    # for i in range(n):
		#     fast = fast.next
	    # if not fast: return head.next
	    # while fast.next:
		#     fast, slow = fast.next, slow.next
	    # slow.next = slow.next.next
	    # return head