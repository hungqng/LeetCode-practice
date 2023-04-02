# 349. Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2)) # Python set operation

        # Solution 2 brute force
        # res = []
        # for i in nums1:
        #     if i not in res and i in nums2:
        #         res.append(i)
        # return res

        # Solution 3 dictionary/hashmap
        # res = []
        # map = {}
        # for i in nums1:
        #     map[i] = map[i]+1 if i in map else 1
        # for j in nums2:
        #     if j in map and map[j] > 0:
        #         res.append(j)
        #         map[j] = 0
        # return res

        # Solution 4 sort two lists then use two pointer to search common elements
        # res = []
        # nums1.sort()
        # nums2.sort()
        # i = j = 0
        # while (i < len(nums1) and j < len(nums2)):
        #     if nums1[i] > nums2[j]:
        #         j += 1
        #     elif nums1[i] < nums2[j]:
        #         i += 1
        #     else:
        #         if not (len(res) and nums1[i] == res[len(res)-1]):
        #             res.append(nums1[i])
        #         i += 1
        #         j += 1
        # return res