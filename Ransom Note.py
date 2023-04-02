# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = sorted(list(ransomNote))
        mag = sorted(list(magazine))
        
        for char in mag:
            if ran and char == ran[0]:
                ran.pop(0)
        if ran:
            return False
        else:
            return True

        # Solution 2
        #return (Counter(ransomNote) - Counter(magazine)) == {}

        # Solution 3
        # for i in set(ransomNote):
        #     if ransomNote.count(i) > magazine.count(i):
        #         return False
        # return True