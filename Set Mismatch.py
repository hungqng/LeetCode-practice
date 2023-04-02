# 645. Set Mismatch

# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rep, mis = None, None
        lookup = Counter(nums)
        
        for i in range(1, len(nums) + 1):
            if i not in lookup:
                mis = i
            if lookup[i] > 1:
                rep = i
        return [rep,mis]

        # Solution 2
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]

        # Solution 3
        n = len(nums)    
        s = n*(n+1)//2   # This code will calculate sum of 1-n numbers. please refer to Arithmetic Progression from Maths
        miss = s - sum(set(nums))  # set(num) will return unique elements from the list and the sum(set(nums)) will calculate the sum of unique elements from the list.
        duplicate = sum(nums) + miss - s # sum(nums) + miss no - sum of 1-n numbers will give us the duplicate
        return [duplicate, miss]