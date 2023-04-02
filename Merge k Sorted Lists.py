# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
        
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

        # Divide and Conquer
    #     if not lists:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #     mid = len(lists) // 2
    #     l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
    #     return self.merge(l, r)
    
    # def merge(self, l, r):
    #     dummy = p = ListNode()
    #     while l and r:
    #         if l.val < r.val:
    #             p.next = l
    #             l = l.next
    #         else:
    #             p.next = r
    #             r = r.next
    #         p = p.next
    #     p.next = l or r
    #     return dummy.next
    
    # def merge1(self, l, r):
    #     if not l or not r:
    #         return l or r
    #     if l.val< r.val:
    #         l.next = self.merge(l.next, r)
    #         return l
    #     r.next = self.merge(l, r.next)
    #     return r

        # heapq
    #     h = []
	# head = tail = ListNode(0)
	# for i in range(len(lists)):
	# 	heapq.heappush(h, (lists[i].val, i, lists[i]))

	# while h:
	# 	node = heapq.heappop(h)
	# 	node = node[2]
	# 	tail.next = node
	# 	tail = tail.next
	# 	if node.next:
	# 		i+=1
	# 		heapq.heappush(h, (node.next.val, i, node.next))

	# return head.next